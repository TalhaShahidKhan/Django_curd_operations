from django.forms import ModelForm
from product.models import Product

class ProductAddForm(ModelForm):
  class Meta:
    model=Product
    fields='__all__'