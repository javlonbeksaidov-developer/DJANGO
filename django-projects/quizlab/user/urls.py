from django.urls import path

from .views import ProfilePage

app_name = "user"

urlpatterns = [
    path("", ProfilePage.as_view(), name="profile")
]