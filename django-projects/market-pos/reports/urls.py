from django.urls import path

from .views import ReportsPage

app_name = "reports"

urlpatterns = [
    path("/", ReportsPage.as_view(), name="reports")
]
