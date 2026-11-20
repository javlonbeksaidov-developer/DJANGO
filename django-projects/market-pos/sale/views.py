from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class SalePage(LoginRequiredMixin, TemplateView):
    template_name = "sale.html"


class ReturnPage(TemplateView):
    template_name = "return.html"
