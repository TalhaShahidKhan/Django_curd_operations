from django.forms import ModelForm
from booklist.models import ListingsOfBook


class AddBookForm(ModelForm):
  class Meta:
    model=ListingsOfBook
    fields="__all__"
