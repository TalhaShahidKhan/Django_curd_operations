from django.shortcuts import render,redirect
from post.models import Post
from post.forms import PostCreateForm
# Create your views here.
#listing Post
def all_posts(request):
  post=Post.objects.all()
  context={
    "post":post
  }
  return render(request, 'postlist.html', context)


# Create post 
def create_post(request):
  form=PostCreateForm()
  context={
    "form":form
  }
  if request.method =="POST":
    form=PostCreateForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/crud2")
  return render(request, 'createpost.html',context)


def detail_post(request,pk):
  data=Post.objects.get(id=pk)
  context={
    "data":data
  }
  return render(request, "postdetails.html",context)


def update_post(request,pk):
  post=Post.objects.get(id=pk)
  form=PostCreateForm(instance=post)
  context={
    "form":form
  }
  if request.method == "POST":
    form=PostCreateForm(request.POST, instance=post, files=request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/crud2")

  return render(request, "updatepost.html",context)


def delt_post(request,pk):
  post=Post.objects.get(id=pk)
  post.delete()
  return render(request, 'deltbook.html')