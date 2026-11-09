from django.urls import path

from .views import staff_page

app_name = "staff"

urlpatterns = [
    path("management/", staff_page, name="management")
]