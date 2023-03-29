from django.db import models
from .import Category


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    discription=models.CharField(max_length=200,null=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    img=models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name