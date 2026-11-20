from django.shortcuts import render
from django.views.generic import TemplateView


class Users(TemplateView):
    template_name = "users.html"


class Profile(TemplateView):
    template_name = "profile.html"