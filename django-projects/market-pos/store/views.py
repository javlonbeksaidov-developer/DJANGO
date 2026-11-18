from django.shortcuts import render
from django.views.generic import TemplateView


class Products(TemplateView):
    template_name = "products.html"


class Store(TemplateView):
    template_name = "store.html"
