from django.urls import path

from .views import ProfilePage, UpdatePage

app_name = "user"

urlpatterns = [
    path("", ProfilePage.as_view(), name="profile"),
    path("profile-update/", UpdatePage.as_view(), name="profile_update")
]