from django import forms
from .models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ['long_url']
        # widgets = {
        #     'long_url': forms.Textarea(attrs={'placeholder': 'long url'})
        # }
