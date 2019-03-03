from django.shortcuts import render


def enroll(request):
    '在线报名'
    title = '在线报名'
    return render(request, 'usercourse/enroll.html', locals())
