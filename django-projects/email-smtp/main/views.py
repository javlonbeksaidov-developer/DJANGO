from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.


def home_page(request):
    return render(request, "index.html")


def send_message(request):
    subject = "SMTP lesson"
    message = "Email xabar yuborish."
    from_email = None
    recievers = [
        "azmilanbarsa55@gmail.com",
        "saidjalol1908@gmail.com",
        "javlonbeksaidov09@gmail.com",
        "obidovyashnar6@gmail.com",
        "akbaraminjonov2@gmail.com",
        "gulhayot.osarova777@gmail.com",
    ]

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recievers,
        )
        return HttpResponse(content="Sent all !")
    except Exception as e:  # noqa: BLE001
        return HttpResponse(content=f"Error: {e}")


def send_html_email(request):
    data = {"username": "Saidov Javlon"}

    subject = "SMTP lesson"
    message = render_to_string("email/email.html", data)
    from_email = None
    recievers = [
        "azmilanbarsa55@gmail.com",
        "saidjalol1908@gmail.com",
        "javlonbeksaidov09@gmail.com",
        "obidovyashnar6@gmail.com",
        "akbaraminjonov2@gmail.com",
        "gulhayot.osarova777@gmail.com",
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
