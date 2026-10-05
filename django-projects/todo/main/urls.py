from django.urls import path

from .views import welcome_page

app_name = "main"

urlpatterns  = [
    path("", welcome_page, name="home page")
]