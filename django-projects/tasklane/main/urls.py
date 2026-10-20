from django.urls import path

from .views import *

app_name = "main"

urlpatterns = [
    path("", index_page, name="index"),
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("profile/", profile_page, name="profile"),
    path("manage/", manage_page, name="manage"),
]
