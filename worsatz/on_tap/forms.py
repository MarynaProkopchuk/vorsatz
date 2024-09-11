from django import forms
from .models import OnTap

class OnTapForm(forms.ModelForm):
    class Meta:
        model = OnTap
        fields = ['name', 'production', 'alcohol', 'ibu', 'style', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'production': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter production'}),
            'alcohol': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter alcohol percentage'}),
            'ibu': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter IBU'}),
            'style': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter style'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
        }