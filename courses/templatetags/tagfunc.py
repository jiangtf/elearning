# -*- coding:utf-8 -*-
# !/usr/bin/env python3
'''自定义过虑器'''
__author__ = 'zween'
__mtime__ = '2019-01-17'

from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter
def removetags(value, arg):
    '清除指定的html标签'
    tags = arg.split()
    for t in tags:
        regstr = r'</?%s[^>]*>' % t
        value = re.sub(regstr, '', value, re.S | re.M)
    return mark_safe(value)
