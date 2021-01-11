from django import forms

from .models import Show, Spent
from autoslug import AutoSlugField


class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['show']
        labels = {'show': ''}


class SpentForm(forms.ModelForm):
    class Meta:
        model = Spent
        fields = ['amount']
        labels = {'amount': ''}


class DeleteSpentForm(forms.ModelForm):
    class Meta:
        model = Spent
        fields = []


class DeleteShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = []
