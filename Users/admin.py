from django.contrib import admin
from .models import User
# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display=['id',"userName","email",'password']
    search_fields=['userName']
    
admin.site.register(User,AdminUser)
