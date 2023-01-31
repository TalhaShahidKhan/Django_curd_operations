from django.db import models

# Create your models here.


class ListingsOfBook(models.Model):
  name=models.CharField(max_length=120)
  price=models.FloatField(null=True,blank=True)
  description=models.TextField()
  image=models.ImageField( upload_to='booklist/images',null=True,blank=True)

  def __str__(self):
    return self.name