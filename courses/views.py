from django.shortcuts import render
from django.http import HttpResponse
from .models import choice_question, completion_question, outside_reading


def index(request):
    return HttpResponse('hello')


def xuanzeti(request):
    '选择题'
    title = '选择题'
    items = choice_question.objects.all()
    return render(request, 'courses/xuanzeti.html', locals())


def tiankongti(request):
    '填空题'
    title = '填空题'
    items = completion_question.objects.all()
    return render(request, 'courses/tiankongti.html', locals())


def kewaiyuedu(request):
    '课外阅读'
    title = '课外阅读'
    items = outside_reading.objects.all()
    return render(request, 'courses/kewaiyuedu.html', locals())
