from django.db import models

# Create your models here.
class User(models.Model):
    userName=models.CharField(max_length=20,blank=False,null=False)
    email=models.EmailField(unique=True,blank=False,null=False)
    password=models.CharField(max_length=128)
    def __str__(self):
        return self.userName
    
    