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