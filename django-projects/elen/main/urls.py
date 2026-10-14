from django.urls import path

from .views import *

app_name = "main"

urlpatterns = [
    path("", index_1, name="index_1"),
    path("index/", index_2, name="index_2"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("fashion/", fashion, name="fashion"),
    path("travel/", travel, name="travel"),
    path("photofgraphy/", photofgraphy, name="photofgraphy"),
]
