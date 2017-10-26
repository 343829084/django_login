# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import Client

# Create your tests here.

class TestAccounti(TestCase):
    def test_basic_addtion(self):
        self.assertEqual(1+1,2)

    def test_user_login(self):
        c = Client()
        response = c.get('/accounts/login')
        self.assertEqual(response.status_code, 200)
        response = c.get('/')
        self.assertEqual(response.status_code, 302)




