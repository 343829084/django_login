# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms

# Create your views here.
@login_required
def index(request):
    return render(request, "index.html",
            {'title':u'主页', 'username':request.user.username})
