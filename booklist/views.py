from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse,reverse_lazy
from booklist.models import ListingsOfBook
from booklist.forms import AddBookForm
# Create your views here.
# Home page
def home_page(request):
  return render(request, 'index.html')
# CRUD-1 Booklist
# Listing Books
def list_book(request):
  booklist=ListingsOfBook.objects.all()
  context={
    "booklist":booklist
  }
  return render(request, 'booklist.html',context)

# Create Books
def create_book(request):
  form=AddBookForm()
  context={
    "form":form
  }
  if request.method =="POST":
    form=AddBookForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/crud1")

  return render (request, 'addbook.html',context)



# Update Book Details
def update_book(request,pk):
  book=ListingsOfBook.objects.get(id=pk)
  form=AddBookForm(instance=book)
  context={
    "form":form
  }
  if request.method =="POST":
    form=AddBookForm(request.POST, instance=book, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/crud1")
  return render(request, 'updatebook.html',context)

# Delete Book 
def delete_book(request,pk):
  book=ListingsOfBook.objects.get(id=pk)
  book.delete()
  return render(request, 'deletebook.html')





# Detail of Book 
def book_details(request,pk):
  book=ListingsOfBook.objects.get(id=pk)
  context={
    "book":book
  }

  return render(request, 'bookdetails.html',context)