from django import forms

from .models import Category


class BookCreateForm(forms.Form):
    title = forms.CharField(
        max_length=120, min_length=5, required=True, initial="O'tgan kunlar"
    )
    category = forms.ChoiceField(choices=[("ilmiy", "Ilmiy"), ("texno", "Texno")])
    price = forms.DecimalField(
        label="Narxi",
        max_value=5000,
        min_value=500,
        decimal_places=2,
    )
    description = forms.CharField(required=True, widget=forms.Textarea())


class QuizCreateForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=5,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Quiz nomini kiriting",
            "class": "form-control"
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Kategoriyani tanlang",
        widget=forms.Select(attrs={
            "class": "form-select"
        })
    )

    started = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local",
            "class": "form-control"
        })
    )

    minutes = forms.IntegerField(
        min_value=10,
        widget=forms.NumberInput(attrs={
            "min": 10,
            "placeholder": "Davomiyligi (daqiqada)",
            "class": "form-control"
        })
    )
