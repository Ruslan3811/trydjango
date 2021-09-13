from django import forms
from .models import Product

# наследование класса ProductForm - child класс, forms.ModelForm - parent class
class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                widget=forms.TextInput(attrs={"placeholder": "title"}))
    # email = forms.EmailField()
    Description = forms.CharField(
                                required=False,
                                widget=forms.Textarea(
                                    attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "new-class-name two",
                                    "rows": 20,
                                    'cols':120
            }
        )
    )
    # Price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title', 
            'Description', 
            # 'Price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "Ruslan" in title:
            return title
        else:
            raise forms.ValidationError("Error name title")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email

class PureDjangoForm(forms.Form):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={"placeholder":"my_title"}))
    Description = forms.CharField(
                                required=False,
                                widget=forms.Textarea(attrs={
                                    "class": "new-class-name two",
                                    "rows": 1,
                                    "cols":10
            }
        )
    )
    Price = forms.DecimalField(initial=199.99)