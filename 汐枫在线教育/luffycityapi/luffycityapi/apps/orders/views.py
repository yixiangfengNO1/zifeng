import logging

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSet
from rest_framework import status
from django.db import transaction

from .serializers import OrderListModelSerializer
from .paginations import OrderListPageNumberPagination
from .models import Order
from .serializers import OrderModelSerializer
from coupon.services import add_coupon_to_redis

logger = logging.getLogger("django")


# Create your views here.
class OrderCreateAPIView(CreateAPIView):
    """创建订单"""
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer


class OrderPayChoicesAPIView(APIView):
    def get(self, request):
        """订单过滤过滤选项"""
        return Response(Order.status_choices)


class OrderListAPIView(ListAPIView):
    """当前登录用户的订单列表"""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListModelSerializer
    pagination_class = OrderListPageNumberPagination

    def get_queryset(self):
        user = self.request.user  # 获取当前登录用户
        query = Order.objects.filter(user=user, is_deleted=False, is_show=True)
        order_status = int(self.request.query_params.get("status", -1))
        status_list = [item[0] for item in Order.status_choices]
        if order_status in status_list:
            query = query.filter(order_status=order_status)

        return query.order_by("-id").all()


class OrderViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def pay_cancel(self, request, pk):
        """取消订单"""
        try:
            order = Order.objects.get(pk=pk, order_status=0)
        except:
            return Response({"eremsg": "当前订单记录不存在或不能取消！"}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                # 1. 查询当前订单是否使用了积分，如果有则恢复
                if order.credit > 0:
                    order.user.credit += order.credit
                    order.user.save()

                # 2. 查询当前订单是否使用了优惠券，如果有则恢复
                obj = order.to_coupon.first()
                if obj:
                    add_coupon_to_redis(obj)

                # 3. 切换当前订单为取消状态
                order.order_status = 2
                order.save()

                return Response({"error": "当前订单已取消！"})

            except Exception as e:
                transaction.savepoint_rollback(save_id)
                logger.error(f"订单无法取消！发生未知错误！{e}")
                return Response({"errmsg": "当前订单无法取消，请联系客服工作人员！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
