from django import forms


class ThemeSelectionForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    theme = forms.ChoiceField(
        required=True,
        choices=[("light-theme", "Light"), ("dark-theme", "Dark")],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
