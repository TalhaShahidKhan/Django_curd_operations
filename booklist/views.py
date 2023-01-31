from django.shortcuts import render
from booklist.models import ListingsOfBook
# Create your views here.
# Home page
def home_page(request):
  return render(request, 'index.html')
# CRUD-1 Booklist

def list_book(request):
  booklist=ListingsOfBook.objects.all()
  context={
    "booklist":booklist
  }
  return render(request, 'booklist.html',context)