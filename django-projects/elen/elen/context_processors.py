from .models import Category


def category_context(request):
    context = {"categories": Category.objects.all()}
    return context
