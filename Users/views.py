from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.hashers import check_password,make_password
from operations.models import Borrow
# Create your views here.
def Register(request):
    message = ""
    if request.method=="POST":
        inputUserName=request.POST.get('userName')
        inputEmail=request.POST.get('email')
        inputPassword=request.POST.get('password')
        inputConfirmPassword=request.POST.get('confirm')
        if inputPassword!=inputConfirmPassword:
            message = "Passwords do not match."
        elif User.objects.filter(email=inputEmail).exists():
            message = "This email is already registered."
        else:
            data=User(userName=inputUserName,email=inputEmail,password=make_password(inputPassword))
            data.save()
            message="Registered successfully!" 
            request.session['user_id']=data.id
            request.session['user_name']=data.userName
            return redirect("Home")
    return render(request,"Users/register.html",{'message':message})
def LogIn(request):
    message=""
    if request.method =="POST":
        inputEmail=request.POST.get('email')
        inputPassword=request.POST.get('password')
        if not User.objects.filter(email=inputEmail).exists():
            message = "The email is not registered."
        else:    
            user=User.objects.filter(email=inputEmail).first()
            if user: # Mean  user is not None (i.e, found in the DataBase)
                if check_password(inputPassword,user.password):
                    request.session['user_id']=user.id # Save id in session table
                    request.session['user_name']=user.userName # Save userName in session table
                    message = f"Welcome back, {user.userName}!"
                    return redirect("Home")
            else:
                 message = "The password is not correct."
    return render(request,'Users/logIn.html',{'message':message})
def LogOut(request):
    request.session.flush()
    return redirect("logIn")

def settings(request):
    message = ''
    try:
        user = User.objects.get(userName=request.session['user_name'])
        book=Borrow.objects.filter(user=user)
    except User.DoesNotExist:
        return redirect('Home')

    if request.method == 'POST':
        new_name = request.POST.get('username')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')

        messages = []

        if new_name:
            user.userName = new_name
            messages.append("User name updated.")
        if new_email:
            user.email = new_email
            messages.append("Email updated.")
        if new_password:
            user.password = make_password(new_password)
            messages.append("Password updated.")

        if messages:
            user.save()
            message = " | ".join(messages)
        else:
            message = "No changes made."

    return render(request, 'Users/settings.html', {"message": message, "user": user,'books':book})
                
                    
                
            