from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/", views.Users.as_view(), name="users"),
    path("users/profile/", views.Profile.as_view(), name="profile"),
]
