from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class StorePage(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "store.html"

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Sizning bu bo'limga kirishga ruxsatingiz yo'q!")
        return redirect("/auth/login")


class ProductsPage(TemplateView):
    template_name = "products.html"
