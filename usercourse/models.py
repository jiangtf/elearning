from django.db import models
from abc import abstractmethod
from users.models import User

from courses.models import grade_course, choice_question, reading_comprehension, completion_question, outside_reading
import django.utils.timezone as timezone


class OrderBase(models.Model):
    '订单基础表'
    register_date = models.DateTimeField('购买时间', default=timezone.now, editable=False)
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='购买者')
    apply_bill = models.BooleanField('是否已经申请了发票', default=False)
    is_draw_bill = models.BooleanField('是否已经开了发票', default=False)
    taitou_type = models.IntegerField('发票类型,1:个人，2：公司', default=1)  # type:
    taitou_text = models.CharField('抬头', max_length=256, default='', null=True, blank=True)
    recognition_id = models.CharField('纳税人识别号', max_length=256, default='', null=True, blank=True)
    email = models.EmailField('收件电子邮箱', max_length=256, default='', null=True, blank=True)
    price = models.IntegerField('价格', default=0)
    invoice_date = models.DateTimeField('申请发票时间', auto_now=True, editable=False)

    def get_order_id(self):
        return self.register_date.strftime('%Y%m%d%H%M%S') + str(self.pk).zfill(6)

    def __str__(self):
        return self.get_order_id()

    @abstractmethod
    def get_name(self):
        return "OrderBase名字"

    @abstractmethod
    def get_goods_url(self):
        return "/"

    class Meta:
        verbose_name = 'o订单'
        verbose_name_plural = 'o订单'
        ordering = ['-register_date']


class GradeCourseOrder(OrderBase):
    '课程学科订单'
    grade_course = models.ForeignKey(grade_course, on_delete=models.CASCADE, blank=True, verbose_name='学科课程')

    def __str__(self):
        return self.get_order_id()

    @abstractmethod
    def get_name(self):
        return self.grade_course.name

    @abstractmethod
    def get_goods_url(self):
        return self.grade_course.get_absolute_url()

    class Meta:
        verbose_name = '课程学科订单'
        verbose_name_plural = '课程学科订单'
        ordering = ['-grade_course']


class Choice_Question_History(models.Model):
    '选择题历史记录表'
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='用户')
    choice_question = models.ForeignKey(choice_question, on_delete=models.CASCADE, blank=True, verbose_name='选择题目')
    answer = models.CharField('用户答案', max_length=256, default='', null=True, blank=True)
    answer_is_true = models.BooleanField('答案是否正确', default=True)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        verbose_name = '选择题历史记录表'
        verbose_name_plural = '选择题历史记录表'
        ordering = ['-add_time']


class Completion_Question_History(models.Model):
    '填空题历史记录表'
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='用户')
    completion_question = models.ForeignKey(completion_question, on_delete=models.CASCADE, blank=True,
                                            verbose_name='填空题目')
    answer = models.CharField('用户答案', max_length=256, default='', null=True, blank=True)
    answer_is_true = models.BooleanField('答案是否正确', default=True)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        verbose_name = '填空题历史记录表'
        verbose_name_plural = '填空题历史记录表'
        ordering = ['-add_time']


class Reading_Comprehension_History(models.Model):
    '阅读理解题目历史记录表'
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='用户')
    reading_comprehension = models.ForeignKey(reading_comprehension, on_delete=models.CASCADE, blank=True,
                                              verbose_name='阅读理解题目')
    answer = models.CharField('用户答案', max_length=256, default='', null=True, blank=True)
    answer_is_true = models.BooleanField('答案是否正确', default=True)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        verbose_name = '阅读理解题目历史记录表'
        verbose_name_plural = '阅读理解题目历史记录表'
        ordering = ['-add_time']


class Outside_Reading_History(models.Model):
    '课外阅读题目历史记录表'
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='用户')
    outside_reading = models.ForeignKey(outside_reading, on_delete=models.CASCADE, blank=True, verbose_name='课外阅读题目')
    answer = models.CharField('用户答案', max_length=256, default='', null=True, blank=True)
    answer_is_true = models.BooleanField('答案是否正确', default=True)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        verbose_name = '课外阅读题目历史记录表'
        verbose_name_plural = '课外阅读题目历史记录表'
        ordering = ['-add_time']
