from django.shortcuts import render


def index(request):
    '首页'
    title = '首页'
    return render(request, 'home/index.html', locals())
