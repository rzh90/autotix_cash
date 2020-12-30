from django import forms

from .models import Show, Spent


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
