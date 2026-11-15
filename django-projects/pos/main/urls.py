from django.urls import path

from .views import CategoryPage, HomePage, OmborPage, SotuvPage, SotuvTarixPage

app_name = "main"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("sotuv/", SotuvPage.as_view(), name="sotuv"),
    path("ombor/", OmborPage.as_view(), name="ombor"),
    path("category/", CategoryPage.as_view(), name="category"),
    path("stuv-tarix/", SotuvTarixPage.as_view(), name="sotuv_tarix"),
]