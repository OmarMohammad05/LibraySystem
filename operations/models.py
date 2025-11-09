from django.db import models
from Users.models import User

# Create your models here.
class Box(models.Model):
    book_name=models.CharField(max_length=100,blank=False,null=False)
    author=models.CharField(max_length=100,blank=False,null=False)
    category=models.CharField(max_length=50,blank=True,null=False)
    copy=models.IntegerField(default=1)
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
    ]
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='available')
    def __str__(self):
        return f"{self.book_name} by {self.author}"
  
class Borrow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Box,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True) # When register recodr direct put date.
    return_date = models.DateField(blank=True, null=True)  # u can be null , when user return book.
    def __str__(self):
        return f"{self.user.userName} borrowed {self.book.book_name} on {self.borrow_date}"



