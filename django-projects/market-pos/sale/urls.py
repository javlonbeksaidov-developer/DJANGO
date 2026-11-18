from django.urls import path

from .views import ReturnPage

app_name = "sale"

urlpatterns = [
    path("return/", ReturnPage.as_view(), name="return"),
]