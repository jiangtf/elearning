from django.shortcuts import render
from courses.models import choice_question, completion_question, outside_reading, reading_comprehension


def index(request):
    '首页'
    title = '首页'
    xuanze = choice_question.objects.count()  # 选择题
    tiankong = completion_question.objects.count()  # 填空题
    kewaiyd = outside_reading.objects.count()  # 课外阅读
    yuedulijie = reading_comprehension.objects.count()  # 阅读理解
    return render(request, 'home/index.html', locals())
