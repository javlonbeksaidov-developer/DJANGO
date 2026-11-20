from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView


class ReportsPage(LoginRequiredMixin, UserPassesTestMixin,TemplateView):
    template_name = "reports.html"
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        return redirect("/auth/login")