from django.urls import path

from . import views

app_name = "sale"

urlpatterns = [
    path("", views.SalePage.as_view(), name="sale"),
    path("return/", views.ReturnPage.as_view(), name="return"),
]
