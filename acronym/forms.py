from django import forms
from django.forms import Textarea


class TextForm(forms.Form):
    input = forms.CharField(widget=Textarea(attrs={'rows': 6, 'cols': 80}))
