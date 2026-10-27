from django.urls import path

from .views import (
    login_page,
    logout_page,
    password_change_page,
    profile_page,
    register_page,
)

app_name = "auth_app"

urlpatterns = [
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("register/", register_page, name="register"),
    path("profile/", profile_page, name="profile"),
    path("password-change/", password_change_page, name="password_change")


]
