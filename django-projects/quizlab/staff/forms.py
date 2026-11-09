from django import forms

from quiz.models import Quizs


class QuizCreateForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"datetime-local"}))
    class Meta:
        model = Quizs
        fields = ["title", "start_time", "minutes", "science"]  # noqa: RUF012
