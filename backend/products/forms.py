from django import forms

from .models import Product

class ProductForm(form.ModelForm):
  class Meta:
    model = Product
    fields = [
      'title',
      'content',
      'price'
    ]