from django.shortcuts import render
from django.views.generic import TemplateView


class SalePage(TemplateView):
    template_name = "sale.html"


class ReturnPage(TemplateView):
    template_name = "return.html"
