""" URL Shortener forms. """

from django import forms
from .models import ShortUrl


class ShorturlForm(forms.ModelForm):

    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form", "placeholder": "Paste link to shorten!"}
    ))

    class Meta:
        model = ShortUrl

        fields = ('long_url',)
