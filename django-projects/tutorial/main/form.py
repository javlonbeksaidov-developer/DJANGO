from django import forms


class BookCreateForm(forms.Form):
    title = forms.CharField(max_length=120, min_length=5, required=True, initial="O'tgan kunlar")
    category = forms.ChoiceField(choices=[("ilmiy", "Ilmiy"), ("texno", "Texno")])
    description = forms.CharField(required=True, widget=forms.Textarea())


