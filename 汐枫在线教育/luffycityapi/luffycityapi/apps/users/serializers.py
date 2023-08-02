import re, constants
from rest_framework import serializers
from django_redis import get_redis_connection

from tencentcloudapi import TencentCloudAPI
from .models import User, UserCourse
from authenticate import generate_jwt_token


class UserRegisterModelSerializer(serializers.ModelSerializer):
    """
    用户注册的序列化器
    """
    re_password = serializers.CharField(required=True, write_only=True)
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True)
    token = serializers.CharField(read_only=True)
    ticket = serializers.CharField(write_only=True)
    randstr = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["mobile", "password", "re_password", "sms_code", "token", "ticket", "randstr"]
        extra_kwargs = {
            "mobile": {
                "required": True, "write_only": True
            },
            "password": {
                "required": True, "write_only": True, "min_length": 6, "max_length": 16,
            },
        }

    def validate(self, data):
        """验证客户端数据"""
        # 手机号格式验证
        mobile = data.get("mobile", None)
        if not re.match("^1[3-9]\d{9}$", mobile):
            raise serializers.ValidationError(detail="手机号格式不正确！", code="mobile")

        # 密码和确认密码
        password = data.get("password")
        re_password = data.get("re_password")
        if password != re_password:
            raise serializers.ValidationError(detail="密码和确认密码不一致！", code="password")

        # 手机号是否已注册
        try:
            User.objects.get(mobile=mobile)
            raise serializers.ValidationError(detail="手机号已注册！", code="mobile")
        except User.DoesNotExist:
            pass

        # 验证腾讯云的滑动验证码
        api = TencentCloudAPI()
        # 视图中的request对象，在序列化器中使用 self.context["request"]
        result = api.captcha(
            data.get("ticket"),
            data.get("randstr"),
            self.context["request"]._request.META.get("REMOTE_ADDR"),
        )

        if not result:
            raise serializers.ValidationError(detail="滑动验证码校验失败！", code="verify")

        # 验证短信验证码
        redis = get_redis_connection("sms_code")
        code = redis.get(f"sms_{mobile}")
        if code is None:
            """获取不多验证码，则表示验证码已经过期了"""
            raise serializers.ValidationError(detail="验证码失效或已过期！", code="sms_code")

        # 从redis提取的数据，字符串都是bytes类型，所以decode
        if code.decode() != data.get("sms_code"):
            raise serializers.ValidationError(detail="短信验证码错误！", code="sms_code")

        # 删除掉redis中的短信，后续不管用户是否注册成功，至少当前这条短信验证码已经没有用处了
        redis.delete(f"sms_{mobile}")

        return data

    def create(self, validated_data):
        """保存用户信息，完成注册"""
        mobile = validated_data.get("mobile")
        password = validated_data.get("password")

        user = User.objects.create_user(
            username=mobile,
            mobile=mobile,
            avatar=constants.DEFAULT_USER_AVATAR,
            password=password,
        )

        # 注册成功以后，免登陆, 生成 jwt token
        user.token = generate_jwt_token(user)
        return user


class UserCourseModelSerializer(serializers.ModelSerializer):
    """用户课程信息序列化器"""
    course_cover = serializers.ImageField(source="course.course_cover")
    course_name = serializers.CharField(source="course.name")
    chapter_name = serializers.CharField(source="chapter.name", default="")
    chapter_id = serializers.IntegerField(source="chapter.id", default=0)
    chapter_orders = serializers.IntegerField(source="chapter.orders", default=0)
    lesson_id = serializers.IntegerField(source="lesson.id", default=0)
    lesson_name = serializers.CharField(source="lesson.name", default="")
    lesson_orders = serializers.IntegerField(source="lesson.orders", default=0)
    course_type = serializers.IntegerField(source="course.course_type", default=0)
    get_course_type_display = serializers.CharField(source="course.get_course_type_display", default="")

    class Meta:
        model = UserCourse
        fields = [
            "course_id", "course_cover", "course_name", "study_time",
            "chapter_id", "chapter_orders", "chapter_name",
            "lesson_id", "lesson_orders", "lesson_name",
            "course_type", "get_course_type_display", "progress",
            "note", "qa", "code"
        ]
