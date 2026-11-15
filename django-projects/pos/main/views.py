from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"


class SotuvPage(TemplateView):
    template_name = "sotuv.html"


class OmborPage(TemplateView):
    template_name = "ombor.html"


class CategoryPage(TemplateView):
    template_name = "kategoriyalar.html"


class SotuvTarixPage(TemplateView):
    template_name = "sotuvlar.html"
