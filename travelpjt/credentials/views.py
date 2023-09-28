from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.

def register(request):

    if request.method == 'POST':

        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        psw = request.POST['psw']
        cpassword = request.POST['cpassword']

        if psw==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=psw)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']
        user=auth.authenticate(username=username,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
