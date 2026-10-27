from django.shortcuts import redirect, render

from .models import Posts

# Create your views here.


def post_create_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.POST.get("image")

        post = Posts.objects.create(
            title=title, description=description, image=image, user=request.user
        )
        post.save()
        return redirect("main:home")

    return render(request, "post/create.html")
