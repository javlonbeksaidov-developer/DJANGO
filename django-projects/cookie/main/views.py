from django.shortcuts import redirect, render

from .forms import ThemeSelectionForm


def home_page(request):

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # Cookie saqlash
        if form_type == "theme_selected":
            form = ThemeSelectionForm(request.POST)

            if form.is_valid():
                response = redirect("/")

                response.set_cookie(
                    key="theme",
                    value=form.cleaned_data["theme"],
                    max_age=60 * 60 * 24 * 30,
                )

                return response

        # Cookie o'chirish
        elif form_type == "clear_cookies":
            response = redirect("/")
            response.delete_cookie("theme")

            return response

    form = ThemeSelectionForm()

    data = {
        "themeForm": form,
        "theme": request.COOKIES.get("theme", "light-theme"),
    }

    return render(request, "index.html", context=data)
