# -*- coding:utf-8 -*-
# !/usr/bin/env python3
'''用户课程模块路由'''
__author__ = 'zween'
__mtime__ = '2019-03-03'
from django.urls import path
from .views import enroll

urlpatterns = [
    path('enroll/', enroll, name='enroll'),
]
