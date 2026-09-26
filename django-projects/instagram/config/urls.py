"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def main(request):
    return render(request, "index.html")

def home(request):
    return HttpResponse(content="Home Page")

def vedio(request):
    return HttpResponse(content="Vedio Page")

def chat(request):
    return HttpResponse(content="Chat Page")

def search(request):
    return HttpResponse(content="Search Page")

def profile(request):
    return HttpResponse(content="Profile Page")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main, name="main_page"),

    path("home/", home, name="home_page"),
    path("vedio/", vedio, name="vedio_page"),
    path("chat/", chat, name="chat_page"),
    path("search/", search, name="search_page"),
    path("profile/", profile, name="profile_page"),
]
