from django import forms
from .models import Product


# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     description = forms.CharField(max_length=400)
#     price = forms.FloatField(min_value=0)
#     image = forms.ImageField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'product_count', 'image']
