from datetime import datetime

from django.shortcuts import render

from .models import Article, Category

# Create your views here.


def home_page(request):
    data = {}
    data["articles"] = Article.objects.all()
    data["date"] = datetime.now()

    return render(request, "index.html", context=data)


def article_detail_page(request, pk):
    data = {}
    data["article"] = Article.objects.get(id=pk)
    data["date"] = datetime.now()

    return render(request, "article_detail.html", context=data)


def article_create_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        image = request.POST.get("image")
        category = request.POST.get("category")

        new_article = Article.objects.create(
            title=title, text=text, image=image, category=category
        )
        new_article.save()

    data = {}
    data["categies"] = Category.objects.all()

    return render(request, "article_create.html", context=data)
