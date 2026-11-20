from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path('reports/', views.ReportsPage.as_view(), name='reports_page')
]