from django.urls import path

from .views import index, post_create_page

app_name = 'posts'

urlpatterns = [
    path('', index, name="index"),
    path('create/', post_create_page, name="post_create")
]