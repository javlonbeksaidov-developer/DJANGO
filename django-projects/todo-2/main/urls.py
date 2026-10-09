from django.urls import path

from .views import home_page

app_name = 'main'

urlpatterns = [
    path('', view=home_page, name="home_page"),
]