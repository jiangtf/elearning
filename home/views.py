from django.shortcuts import render
from courses.models import choice_question, completion_question, outside_reading, reading_comprehension


def index(request):
    title = 'elearning在线学习移动端'
    return render(request, 'home/index.html', locals())


def testing(request):
    '测试'
    title = '在线测试'
    xuanze = choice_question.objects.count()  # 选择题
    tiankong = completion_question.objects.count()  # 填空题
    kewaiyd = outside_reading.objects.count()  # 课外阅读
    yuedulijie = reading_comprehension.objects.count()  # 阅读理解
    return render(request, 'home/testing.html', locals())
