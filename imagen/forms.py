from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'imagen']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'})
        }
        
        