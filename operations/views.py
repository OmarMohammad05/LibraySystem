from django.shortcuts import render,redirect
from .models import Box,Borrow
from Users.models import User
from django.utils import timezone# Create your views here.

#Don’t touch it… it’s in production!
def Home(request):
    if 'user_id' not in request.session:
        return redirect('logIn')
    name=request.session.get("user_name")
    return render(request,'operations/home_operations.html',{"userName":name})

def ViewBooks(request):
    books=Box.objects.all()
    return render(request,'operations/view_books.html',{"books":books})

def BorrowBook(request):
    message = ""
    if request.method=="POST":
        inputBook=request.POST.get('book_name')
        inputName=request.POST.get('name')
        if inputName==request.session['user_name']:
            user=User.objects.filter(userName=inputName).first()
            if not user:
                message = "User not found!"
            else:
                book=Box.objects.filter(book_name=inputBook,status='available').first()
                if not book:
                    message = "Book not found!"
                else:
                    Borrow.objects.create(user=user,book=book)
                    book.copy-=1
                    if book.copy==0:
                        book.status="borrowed"
                    book.save()    
                    message = f"{user.userName} borrowed '{book.book_name}' successfully!"
        else:
            message='The name is not match with this account'            
                        
    return render(request,'operations/borrow_book.html',{'message':message})

def ReturnBook(request):
    message=''
    if request.method=="POST":
        input_book=request.POST.get("book_name")
        input_name=request.POST.get("name")
        if input_name == request.session['user_name']:
            user=User.objects.filter(userName=input_name).first()        
            if not user:
                message = "User not found."
            else:
                book=Box.objects.filter(book_name=input_book).first()
                if not book:
                    message="Book not find"
                else:    
                    borrow_record =Borrow.objects.filter(user=user,book=book,return_date__isnull=True).first()
                    if not borrow_record :
                        message = "This user has not borrowed this book."
                    else:
                        book.copy+=1        
                        book.status='available'
                        book.save()
                        borrow_record.return_date=timezone.now()   
                        borrow_record.save() 
                        message = f"{user.userName} returned '{book.book_name}' successfully!"
        else:
            message='The name is not match with this account'                 
    return render(request,'operations/return_book.html',{'message':message})