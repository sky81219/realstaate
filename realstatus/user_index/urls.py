from django.urls import path

urlpatterns = [
    path("register/", name="register"),
    path("login/", name="login"),
    path("logout/", name="logout")
]