from django import forms

class SearchForm(forms.Form):
    search = forms.CharField()

class ProductForm(forms.Form):
    name  = forms.CharField(label='ชื่อสินค้า', required=True)
    price = forms.CharField(label='ราคา', required=True)
    color = forms.CharField(label='สี', required=False)
    stock = forms.CharField(label='คงเหลือ', required=False)