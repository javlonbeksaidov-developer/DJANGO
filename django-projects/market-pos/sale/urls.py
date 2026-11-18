from django.urls import path

from .views import ReturnPage, SalePage

app_name = "sale"

urlpatterns = [
    path("sale/", SalePage.as_view(), name="sale"),
    path("return/", ReturnPage.as_view(), name="return"),
]