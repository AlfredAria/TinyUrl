# forms.py
from django import forms
from url.models import LongUrl

class LongUrlForm(forms.ModelForm):
    class Meta:
        model = LongUrl
        fields = ('url', )