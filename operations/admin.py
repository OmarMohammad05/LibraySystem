from django.contrib import admin
from .models import Box,Borrow
# Register your models here.
class AdminBox(admin.ModelAdmin):
    list_display=['id','book_name','author','category','copy','status']
    search_fields=['book_name']
admin.site.register(Box,AdminBox)

class AdminBorrow(admin.ModelAdmin):
    list_display=['id','user','book','borrow_date','return_date']
    search_fields=['book.book_name']
    
admin.site.register(Borrow,AdminBorrow)    

admin.site.site_header="Administrator"