# -*- coding:utf-8 -*-
# !/usr/bin/env python3
'''课程表路由'''
__author__ = 'zween'
__mtime__ = '2019-01-16'
from django.urls import path
from .views import index, kewaiyuedu

urlpatterns = [
    path('', index),
    path('kewaiyuedu/', kewaiyuedu, name='kewaiyuedu')
]
