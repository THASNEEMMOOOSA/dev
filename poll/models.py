from django.db import models

# Create your models here.
class Userinfo(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone=models.IntegerField(null=True)
    date=models.DateField(null=True)

    # def __str__(self):
    #     return f"{self.firstname} {self.lastname}"