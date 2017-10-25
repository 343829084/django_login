#!/usr/bin/python
#-*-coding:utf-8-*-

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import LoginForm,RegisterForm
from django.views.decorators.csrf import csrf_protect
from models import User
from django.contrib.auth import logout
from django.contrib import auth
def userlogin(request):
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        print "userlogin name=",form['username']
        captcha = form['captcha']
        print "captcha =",captcha
        if form.is_valid():
            return render(request, "index.html", {"form":form})
        else:
            print "form is not valid"
            return render(request, 'accounts/login.html', {'captcha':captcha, "form":form})
    else:
        form = LoginForm()
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

    form = LoginForm()
    captcha = form['captcha']
    return render(request,'accounts/login.html', {"captcha":captcha})


def register(request):
    if request.method == 'POST':
        uf = RegisterForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            password2 = uf.cleaned_data['password2']
            if not User.objects.all().filter(username=username):
                user = User()
                user.username = username
                user.set_password(password)
                user.save()
                form = LoginForm()
                captcha = form['captcha']
                return render(request, "accounts/login.html", {"captcha":captcha})
    else:
        form = RegisterForm()
        return render(request, "accounts/register.html", {"form":form})

@login_required
def logout(request):
    auth.logout(request) # Redirect to a success page.
    form = LoginForm()
    captcha = form['captcha']
    return render(request,"accounts/login.html",{"captcha":captcha})
