from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .models import Posts

# Create your views here.


def post_create_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        post = Posts.objects.create(
            title=title, description=description, image=image, user=request.user
        )
        post.save()

        image_url = request.build_absolute_uri(post.image.url) if post.image else None

        data = {
            "post": post,
            "image_url": image_url,
        }
        Email_Post.send_mail_create_post(data)
        return redirect("main:home")

    return render(request, "post/create.html")


def post_views_page(request):
    post = Posts.objects.all()
    context = {"posts": post}
    return render(request, "post/post_views.html", context)


class Email_Post:
    @staticmethod
    def send_mail_create_post(data: dict):
        subject = "Create new post"
        message = render_to_string("post/email_post.html", data)
        from_email = None
        recievers = [
            "javlonbeksaidov09@gmail.com",
        ]

        try:
            email = EmailMultiAlternatives(
                subject=subject, body=message, from_email=from_email, to=recievers
            )
            email.attach_alternative(message, "text/html")
            email.send()
            return HttpResponse(content="Sent all !")
        except Exception as e:  # noqa: BLE001
            return HttpResponse(content=f"Error: {e}")
