from django.db import models

class user_inv(models.Model):
    '用户上下级关系'
    name = models.CharField(max_length=50, verbose_name='学科')
    order = models.IntegerField('排序号', default=0)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        verbose_name = u'B学科'
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.name
# Create your models here.
