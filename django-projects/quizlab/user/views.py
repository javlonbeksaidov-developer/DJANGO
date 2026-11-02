from django.shortcuts import render
from django.views.generic import DetailView, UpdateView

from .models import Profile

# Create your views here.


class ProfilePage(DetailView):
    template_name = "profile.html"
    model = Profile
    context_object_name = "profile"

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class UpdatePage(UpdateView):
    model = Profile
    template_name = "profile.html"
    fields = ["about", "profile_image"]  # noqa: RUF012

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.request.user
        user.first_name = self.request.POST.get("first_name")
        user.last_name = self.request.POST.get("last_name")
        user.email = self.request.POST.get("email")
        user.save()

        return response

    def get_success_url(self):
        return self.request.path