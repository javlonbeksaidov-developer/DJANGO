from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from post.models import Posts

# Create your views here.


@login_required
def home_page(request):
    post = Posts.objects.all()
    context = {"posts": post}
    return render(request, "index.html", context)
