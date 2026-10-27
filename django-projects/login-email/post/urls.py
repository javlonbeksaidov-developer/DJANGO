from django.urls import path

from .views import post_create_page

app_name = 'posts'

urlpatterns = [
    path('create/', post_create_page, name="post_create")
]