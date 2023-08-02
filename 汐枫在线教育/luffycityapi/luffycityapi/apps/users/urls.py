from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path("login/", views.LoginAPIView.as_view(), name="login"),
    re_path(r"^mobile/(?P<mobile>1[3-9]\d{9})/$", views.MobileAPIView.as_view()),
    path("register/", views.UserAPIView.as_view()),
    re_path(r"^sms/(?P<mobile>1[3-9]\d{9})/$", views.SMSAPIView.as_view()),
    path("course/", views.CourseListAPIView.as_view()),
    re_path("^course/(?P<course_id>\d+)/$", views.UserCourseAPIView.as_view()),
    path("lesson/", views.StudyLessonAPIView.as_view()),
    path("progress/", views.StudyProgressAPIView.as_view()),
]

# obtain_jwt_token实际上就是 rest_framework_jwt.views.ObtainJSONWebToken.as_view()

# 登录视图，获取access_token
# obtain_jwt_token = ObtainJSONWebToken.as_view()
# 刷新token视图，依靠旧的access_token生成新的access_token
# refresh_jwt_token = RefreshJSONWebToken.as_view()
# 验证现有的access_token是否有效
# verify_jwt_token = VerifyJSONWebToken.as_view()
