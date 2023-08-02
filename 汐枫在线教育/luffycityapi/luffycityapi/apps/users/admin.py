from django.contrib import admin
from .models import User, Credit


# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    """用户的模型管理器"""
    list_display = ["id", "username", "avatar_small", "money", "credit"]
    list_editable = ["credit"]

    def save_model(self, request, obj, form, change):
        if change:
            """更新数据"""
            user = User.objects.get(pk=obj.id)
            has_credit = user.credit  # 原来用户的积分数据
            new_credit = obj.credit  # 更新后用户的积分数据

            Credit.objects.create(
                user=user,
                number=int(new_credit - has_credit),
                operation=2,
            )

        obj.save()

        if not change:
            """新增数据"""
            Credit.objects.create(
                user=obj.id,
                number=obj.credit,
                operation=2,
            )


admin.site.register(User, UserModelAdmin)


class CreditModelAdmin(admin.ModelAdmin):
    """积分流水的模型管理器"""
    list_display = ["id", "user", "number", "__str__"]


admin.site.register(Credit, CreditModelAdmin)
