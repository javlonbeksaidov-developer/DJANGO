from django.urls import path

from .views import LoginPage, ProfilePage, UsersPage

app_name = "accounts"

urlpatterns = [
    path("login/", LoginPage.as_view(), name="login"),
    path("users/", UsersPage.as_view(), name="users"),
    path("profile/", ProfilePage.as_view(), name="profile"),
]
