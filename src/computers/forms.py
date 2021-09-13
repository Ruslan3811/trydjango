from django import forms
from .models import Computer

class ComputerModelForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = [
            'Name', 
            'Years_of_usage',
            'Price'
        ]
