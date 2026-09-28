from django.urls import path

from .views import like_it, main_picture_view, main_vedio_view

app_name = "main"


urlpatterns = [
    path("pictures/", main_picture_view, name="main_picture_view"),
    path("vedios/", main_vedio_view, name="main_vedio_view"),
    path("like/", like_it, name="like_it"),
]
