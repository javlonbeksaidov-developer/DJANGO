from django.shortcuts import render
from django.views.generic import ListView

from .models import Profile

# Create your views here.

class ProfilePage(ListView):
    template_name = "profile.html"
    model = Profile