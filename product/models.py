from django.db import models

# Create your models here.

class Product(models.Model):
  name=models.CharField( max_length=50)
  description=models.TextField()
  price=models.FloatField()
  in_stock=models.BooleanField()
  number=models.IntegerField()
  image=models.ImageField(upload_to='products/images',null=True,blank=True)


  def __str__(self):
    return self.name