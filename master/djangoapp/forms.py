from django import forms
from .models import Category,Product

class CategoryForm(forms.ModelForm):
    # id = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter unique id '}), required=True)
    category = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Enter Category'}), required=True,
        max_length=200)
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Description About Category '}),
        required=True, max_length=200)

    class Meta:
        model=Category
        fields=('id','category','description')
    
class ProductForm(forms.ModelForm):
    # id = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter unique id '}), required=True)
    #
    product = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name '}),
        required=True)
    supplier = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Detail'}), required=True)
    price = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price of a Product '}), required=True)
    stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stock '}),required=True  )
    class Meta:
        model=Product
        fields=('id','category','product','supplier','price','stock')


