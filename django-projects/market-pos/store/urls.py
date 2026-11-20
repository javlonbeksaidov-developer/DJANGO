from django.urls import path

from . import views

app_name = "store"


urlpatterns = [
    path("", views.StorePage.as_view(), name="store"),
    path("products/", views.ProductsPage.as_view(), name="products")
]
