from django import forms

from .models import Drugs


class DrugsAddForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model = Drugs
        fields = ["name", "category", "description", "amount", "price", "expiry_date"]  # noqa: RUF012
