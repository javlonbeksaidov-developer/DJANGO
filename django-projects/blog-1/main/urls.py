from django.urls import path

from .views import *

app_name = "main"

urlpatterns = [
    path("", home_page, name="home"),
    path("article-detail/<int:pk>", article_detail_page, name="article_detail"),
    path("article-create/", article_create_page, name="article_create"),
]
