from django.shortcuts import render
from django.views.generic import TemplateView


class ReturnPage(TemplateView):
    template_name = "return.html"
