from django.shortcuts import render
from django.views.generic import TemplateView


class ReportsPage(TemplateView):
    template_name = "reports.html"
