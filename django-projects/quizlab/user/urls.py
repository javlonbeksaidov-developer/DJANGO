from django.urls import path

from .views import (
    ProfilePage,
    UpdatePage,
    login_page,
    logout_page,
    password_change_page,
    register_page,
)

app_name = "user"

urlpatterns = [
    path("", ProfilePage.as_view(), name="profile"),
    path("profile-update/", UpdatePage.as_view(), name="profile_update"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("register/", register_page, name="register"),
    path("password-change/", password_change_page, name="password_change"),
]
