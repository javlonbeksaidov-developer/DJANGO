from django.urls import path

from .views import *

app_name = "elen"

urlpatterns = [
    path("", index_1, name="index_1"),
    path("index/", index_2, name="index_2"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("fashion/", fashion, name="fashion"),
    path("travel/", travel, name="travel"),
    path("photography/", photography, name="photography"),
    path("register/", register, name="register"),
    path("login/", login_, name="login")
]
