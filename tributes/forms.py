from django import forms
from .models import Tribute

class TributeForm(forms.ModelForm):
    class Meta:
        model = Tribute
        fields = ['departed', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }