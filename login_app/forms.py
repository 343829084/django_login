#!/usr/bin/python
#-*-coding:utf-8-*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField
import traceback
from django.contrib.auth.hashers import make_password, check_password


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())


    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError('所有项都为必填项')
        elif self.cleaned_data['password2'] != self.cleaned_data['password']:
            raise forms.ValidationError('两次输入密码不一致')
        else:
            cleaned_data = super(RegisterForm, self).clean()
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100,error_messages={'required':u'用户名不能为空'})
    password = forms.CharField(label='密码：',widget=forms.PasswordInput(),error_messages={'required':u'密码不能为空'})
    captcha = CaptchaField(required=True,error_messages={'invalid':u"您输入的验证码不正确"})

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        print "loginform username=",username, " password=", password
        self.user_cache = authenticate(username=username, password=password)
        if self.user_cache is None:
            print "user_cache is none"
            raise forms.ValidationError(u"您输入的用户名或密码不正确!")
        elif not self.user_cache.is_active or not self.user_cache.is_staff:
            print "not active"
            raise forms.ValidationError(u"您输入的用户名不正确!")
        else:
            #user = User.objects.filter(username__exact = username, password__exact = password)
            user = User.objects.get(username__exact = username)
            if not user:
                print "can't find in db"
                raise forms.ValidationError(u'数据库中不存在用户名密码')
            print "user password=",user.password
            if check_password(password, user.password):
                login(self.request,self.user_cache)
        return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
