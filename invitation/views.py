from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
# from .models import choice_question, completion_question, outside_reading


def index(request):
    inbitation.fun()
    return HttpResponse('hello')
    # return render(request, 'invitation/index.html', locals())


# def layout(request):
#     inbitation.fun()
#     # return HttpResponse('hello')
#     return render(request, 'elearning/layout.html', locals())

# def xuanzeti(request):
#     '选择题'
#     title = '选择题'
#     items = choice_question.objects.all()
#     return render(request, 'courses/xuanzeti.html', locals())
#
#
# def tiankongti(request):
#     '填空题'
#     title = '填空题'
#     items = completion_question.objects.all()
#     return render(request, 'courses/tiankongti.html', locals())
#
#
# def kewaiyuedu(request):
#     '课外阅读'
#     title = '课外阅读'
#     items = outside_reading.objects.all()
#     return render(request, 'courses/kewaiyuedu.html', locals())
class inbitation(object):

    def __init__(self):
        pass

    @classmethod
    def fun(cls):
        a = User.objects.all().values()
        print('###########')
        print(a)
        print('###########')
        pass