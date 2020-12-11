from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import auth

def account_login(request):
    if not request.method == 'POST':
        return render(request, "accounts/login.html")
    err={}
    username = request.POST.get('username', '')
    if username == '':
        err['username'] = "username can not be null"
    password = request.POST.get('password', '')
    if password == '':
        err['password'] = "password can not be null"
    print(username)
    print(password)
    if len(err) == 0:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            err['password']= "username or password is wrong!"
    print(err)
    return render(request, "accounts/login.html", {"error": err})

@login_required
def account_logout(request):
    logout(request)
    return redirect("accounts/register.html")

def account_register(request):
    if not request.META['REQUEST_METHOD'] == 'POST':
        render(request, "accounts/register.html")
    try:
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        print('%s\t %s \t %s \t %s ' % (email, username, password1, password2))
        err = []
        if not email or not username or not password1 or not password2:
            err.append("Input infomation can not be null")
            render(request, "accounts/register.html", {"error": err})

        if password1 != password2:
            err.append("Two passward isn't match")
            render(request, "accounts/register.html", {"error": err})

        user = User()
        user.username = username
        user.email = email
        user.set_password(password1)
        try:
            user.save()
        except Exception as err:
            print('User register error \t %s' % (err))
        else:

             newUser = authenticate(username=username, password=password1)
             if newUser is not None:
                  login(request, newUser)
                  print("%s login successfully!" % (username))
                  return redirect("/")
    except Exception as e:
        print(e)

    print("%s login failed!" %(user.username))
    return render(request, "accounts/register.html")
