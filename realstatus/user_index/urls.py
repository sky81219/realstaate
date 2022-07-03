from django.urls import path
from api import serializers
from user_index import views

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("register/", views.create_user_view ,name="register"),
    path("login/", views.login_user_view, name="login"),
    
    # token
    path("token/", serializers.UserLoginObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_obtain_pair"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_obtain_pair"),
]