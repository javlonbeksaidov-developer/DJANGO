from django.urls import path

from .views import post_create_page, post_views_page

app_name = 'posts'

urlpatterns = [
    path('create/', post_create_page, name="post_create"),
    path('all/', post_views_page, name="post_views"),
]