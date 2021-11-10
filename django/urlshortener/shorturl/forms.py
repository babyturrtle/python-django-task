"""URL shortener forms"""

from django import forms
from .models import ShortUrl


class ShorturlForm(forms.ModelForm):
    """Form for creating shortened urls"""

    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "url-form", "placeholder": "Paste link to shorten!"}
    ))

    class Meta:
        model = ShortUrl

        fields = ('long_url',)
