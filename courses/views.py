from django.shortcuts import render
from django.http import HttpResponse
from .models import outside_reading


def index(request):
    return HttpResponse('hello')


def kewaiyuedu(request):
    '课外阅读'
    title = '课外阅读'
    info = outside_reading.objects.last()
    return render(request, 'courses/kewaiyuedu.html', locals())
