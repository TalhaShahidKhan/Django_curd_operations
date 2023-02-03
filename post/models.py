from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()
class Post(models.Model):
  author=models.ForeignKey(User, on_delete=models.CASCADE)
  title=models.CharField(max_length=120)
  description=models.TextField()
  image=models.ImageField(upload_to='post/images',null=True)
  date_posted=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
