# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email')
#admin.site.register(User,UserAdmin)
#admin.site.register(User)
