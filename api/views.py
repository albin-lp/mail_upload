from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.core.mail import send_mail
 

# Create your views here.

def index(request):

    if request.method=="POST":
        uname=request.POST["username"]
        pword = request.POST["password"]
        mail = request.POST["email"]
        user= User.objects.create_user(
            username = uname,
            password=pword,
            email=mail
        )
        login(request,user)
        subject="welcome"
        message='hi {user.username},thanku for opening'
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[mail,]
        send_mail(subject,message,email_from,recipient_list)
        return redirect("/dashboard/")
    
    return render(request,"index.html")


