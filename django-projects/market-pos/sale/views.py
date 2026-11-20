from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView
)

class SalePage(LoginRequiredMixin, TemplateView):
    template_name = "sale.html"