from django.shortcuts import render,redirect
from product.models import Product
from product.forms import ProductAddForm
# Create your views here.
# product listing
def product_list(request):
  product=Product.objects.all()
  context={
    "product":product
  }
  return render(request, 'prodlist.html',context)
# product add
def add_product(request):
  form=ProductAddForm()
  context={
    "form":form
  }
  if request.method == "POST":
    form=ProductAddForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/crud3")
  return render(request, 'addproduct.html',context)


# product details
def details_product(request,pk):
  prod=Product.objects.get(id=pk)
  context={
    "product":prod
  }
  return render(request,'proddetails.html',context)


# product update 
def update_product(request,pk):
  product=Product.objects.get(id=pk)
  form=ProductAddForm(instance=product)
  context={
    "form":form
  }
  if request.method == "POST":
    form=ProductAddForm(request.POST, instance=product, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/crud3")

  return render(request, "updateproduct.html",context)




# Delete product 

def delt_product(request,pk):
  product=Product.objects.get(id=pk)
  product.delete()
  return render(request, 'deltproduct.html')