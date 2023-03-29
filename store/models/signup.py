from django.db import models

# Create your models here.
class Subscribstion(models.Model):
    email=models.EmailField(max_length=30)

    def __str__ (self):
        return self.email
# sign up

class Signup_model(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    mobile_no=models.BigIntegerField(null=True)
    city=models.CharField(max_length=50)
    password=models.CharField(max_length=300)
    cnfpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.email

    @staticmethod 
    def get_customer_by_email(email):
        try:
            return Signup_model.objects.get(email=email)
        except:
            False
