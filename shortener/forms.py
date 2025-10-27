from django import forms
from .models import ShortURL


class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={'placeholder': 'https://example.com/very/long/url', 'size': 60})
        }
        labels = {'original_url': '原始網址'}
