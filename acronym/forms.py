from django import forms


class TextForm(forms.Form):
    email = forms.CharField()
