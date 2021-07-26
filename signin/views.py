from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import logout, login


# Create your views here.


def home(request):
    # return HttpResponse("Welcome")
    if request.method == 'GET':
        return render(request, 'index.html', context={})
    else:
        firstname = request.POST['name'].split(" ")[0]
        lastname = request.POST['name'].split(" ")[1]
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['re_pass']
        UserName = email

        if password == cpassword:
            # UserName = email.split('@')[0]
            u = User(username=UserName, first_name=firstname,
                     last_name=lastname, email=email)  # Django user model
            u.save()
            u.set_password(cpassword)
            u.save()
            # up = UserProfile(user=u, dob=datetime.now(), phone=phone, )
            # up.save()
            return render(request, 'login.html', context={})
        else:
            # messages.error(request, 'password does not match')
            return render(request, 'index.html', context={})


def signin(request):

    if request.method == 'GET':
        # print('in get method')

        return render(request, 'signin.html', context={})
    else:
        # print('In post method')
        username = request.POST['your_name']
        password = request.POST['your_pass']
        # print(username, password)
        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, 'Please check your username and password')
            return render(request, 'login.html', context={})

        else:
            # print(user)

            login(request, user)

            return HttpResponse("Successfully logged in")


def signout(request):
    logout(request)
    return signin(request)
