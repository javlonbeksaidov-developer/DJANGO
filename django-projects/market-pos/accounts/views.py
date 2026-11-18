from django.shortcuts import render
from django.views.generic import TemplateView


class LoginPage(TemplateView):
    template_name = "login.html"


class ProfilePage(TemplateView):
    template_name = "profile.html"


class UsersPage(TemplateView):
    template_name = "users.html"
