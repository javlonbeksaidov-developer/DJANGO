from django.shortcuts import redirect, render

from .forms import ThemeSelectionForm

# Create your views here.


def home_page(request):
    data = {"themeForm": ThemeSelectionForm()}

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "theme_selected":
            form = ThemeSelectionForm(request.POST)

            if form.is_valid():
                responce = redirect("/")
                print(form.cleaned_data["theme"])
                responce.set_cookie("theme", form.cleaned_data["theme"])
                return responce

            if form_type == "clear_cookies":
                responce = redirect("/")
                responce.delete_cookie("theme")
                return responce

    return render(request, "index.html", context=data)
