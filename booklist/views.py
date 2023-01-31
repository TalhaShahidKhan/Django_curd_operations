from django.shortcuts import render
# Create your views here.
# Home page
def home_page(request):
  return render(request, 'index.html')
# CRUD-1 Booklist

def list_book(request):
  return render(request, 'booklist.html')