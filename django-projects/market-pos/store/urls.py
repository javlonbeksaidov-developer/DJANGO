from django.urls import path

from .views import Products, Store

app_name = "store"

urlpatterns = [
    path("store/", Store.as_view(), name="store"),
    path("products/", Products.as_view(), name="products"),
]
