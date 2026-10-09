from django.urls import path

from .views import *

app_name = "main"

urlpatterns = [
    path("", home_page, name="home"),
    path("index/", index, name="index"),
    path("about/", about, name="about"),
    path("author/", author, name="author"),
    path("blank/", blank, name="blank"),
    path("category/", category, name="category"),
    path("contact/", contact, name="contact"),
    path("blog/", blog_post, name="blog_post"),
]
