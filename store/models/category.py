from django.db import models


class Category(models.Model):
 name=models.CharField(max_length=50,null= False)

 def __str__(self):
  return self.name