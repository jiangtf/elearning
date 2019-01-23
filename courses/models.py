from django.db import models

from DjangoUeditor.models import UEditorField


class grade(models.Model):
    '年级'
    name = models.CharField(max_length=50, verbose_name='年级')
    order = models.IntegerField('排序号', default=0)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        verbose_name = u'A年级'
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.name


class subject(models.Model):
    '学科'
    name = models.CharField(max_length=50, verbose_name='学科')
    order = models.IntegerField('排序号', default=0)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        verbose_name = u'B学科'
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.name


class grade_course(models.Model):
    '年级学科学费'
    grade_name = models.ForeignKey(grade, blank=True, null=True, verbose_name='年级', on_delete=models.CASCADE)
    subject_name = models.ForeignKey(subject, blank=True, null=True, verbose_name='学科', on_delete=models.CASCADE)
    price = models.IntegerField('价格', default=0)
    order = models.IntegerField('排序号', default=0)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        unique_together = ("grade_name", "subject_name")
        verbose_name = 'C年级学科学费'
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.grade_name.name + '+' + self.subject_name.name


class grade_course_subject(models.Model):
    'D年级学科题目'
    grade_course = models.ForeignKey(grade_course, verbose_name=u"D年级学科题目", on_delete=models.CASCADE)
    TYPE_CHOICE = (
        (u'C', u'选择'),
        (u'F', u'填空'),
        (u'R', u'阅读理解'),
        (u'K', u'课外阅读'),
    )
    subject_type = models.CharField(max_length=2, choices=TYPE_CHOICE, verbose_name=u"题目类型", )
    show_type = models.CharField(max_length=300, verbose_name=u"题目显示名称", )
    order = models.IntegerField('显示顺序', default=0)
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)

    class Meta:
        unique_together = ("grade_course", "subject_type")
        verbose_name = 'D年级学科题目表'
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.grade_course.__str__() + '+' + self.subject_type


class choice_question(models.Model):
    '选择题库'
    questions_org = models.ForeignKey(grade_course, verbose_name=u"题目分类", on_delete=models.CASCADE)
    name = UEditorField('题目', height=300, width=1000,
                        default=u'', blank=True, imagePath="uploads/images/",
                        toolbars='besttome', filePath='uploads/files/')
    TYPE_CHOICE = (
        (u'S', u'单选'),
        (u'M', u'多选'),
    )
    choice_type = models.CharField(max_length=2, choices=TYPE_CHOICE)

    choice_A = models.CharField(max_length=300, verbose_name=u"题目选项A", )
    choice_B = models.CharField(max_length=300, verbose_name=u"题目选项B", )
    choice_C = models.CharField(max_length=300, verbose_name=u"题目选项C", null=True, blank=True)
    choice_D = models.CharField(max_length=300, verbose_name=u"题目选项D", null=True, blank=True)
    answer = models.CharField(max_length=300, verbose_name=u"题目答案")
    keypoint = models.CharField(max_length=300, verbose_name=u"知识点", null=True, blank=True)
    point = models.IntegerField(default=0, verbose_name=u'题目分值', null=True, blank=True)
    complexity = models.CharField(max_length=300, verbose_name=u"难度", null=True, blank=True)
    show_time = models.CharField(verbose_name=u"题目出现时间填写(月-日的形式：如12-18)", max_length=10, )
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)
    # detail = models.CharField(verbose_name=u"试题解析", max_length=50)
    detail = UEditorField('试题解析', height=100, width=1000,
                          default=u'', blank=True, imagePath="uploads/images/",
                          toolbars='besttome', filePath='uploads/files/')
    order = models.IntegerField('排序号', default=0)

    class Meta:
        verbose_name = u"选择题库"
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.questions_org.__str__() + '(' + self.name + ')'


class completion_question(models.Model):
    '填空题库'
    questions_org = models.ForeignKey(grade_course, verbose_name=u"题目分类", on_delete=models.CASCADE)
    name = UEditorField('题目', height=300, width=1000,
                        default=u'', blank=True, imagePath="uploads/images/",
                        toolbars='besttome', filePath='uploads/files/')
    answer_1 = models.CharField(max_length=300, verbose_name=u"填空答案1")
    answer_2 = models.CharField(max_length=300, verbose_name=u"填空答案2", null=True, blank=True)
    answer_3 = models.CharField(max_length=300, verbose_name=u"填空答案3", null=True, blank=True)
    answer_4 = models.CharField(max_length=300, verbose_name=u"填空答案4", null=True, blank=True)
    answer_5 = models.CharField(max_length=300, verbose_name=u"填空答案5", null=True, blank=True)

    keypoint = models.CharField(max_length=300, verbose_name=u"知识点", null=True, blank=True)
    point = models.IntegerField(default=0, verbose_name=u'题目分值', blank=True)
    complexity = models.CharField(max_length=300, verbose_name=u"难度", null=True, blank=True)
    show_time = models.CharField(verbose_name=u"题目出现时间填写(月-日的形式：如12-18)", max_length=10, )
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)
    # detail = models.CharField(verbose_name=u"试题解析", max_length=500)
    detail = UEditorField('试题解析', height=100, width=1000,
                          default=u'', blank=True, imagePath="uploads/images/",
                          toolbars='besttome', filePath='uploads/files/')
    order = models.IntegerField('排序号', default=0)

    class Meta:
        verbose_name = u"填空题库"
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.questions_org.__str__() + '(' + self.name + ')'


class outside_reading(models.Model):
    '课外阅读'
    questions_org = models.ForeignKey(grade_course, verbose_name=u"题目分类", on_delete=models.CASCADE)
    name = UEditorField('课外阅读', height=300, width=1000,
                        default=u'', blank=True, imagePath="uploads/images/",
                        toolbars='besttome', filePath='uploads/files/')

    keypoint = models.CharField(max_length=300, verbose_name=u"知识点", null=True, blank=True)
    point = models.IntegerField(default=0, verbose_name=u'题目分值', blank=True)
    complexity = models.CharField(max_length=300, verbose_name=u"难度", null=True, blank=True)
    show_time = models.CharField(verbose_name=u"题目出现时间填写(月-日的形式：如12-18)", max_length=10, )
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)
    # detail = models.CharField(verbose_name=u"试题解析", max_length=500)
    detail = UEditorField('试题解析', height=100, width=1000,
                          default=u'', blank=True, imagePath="uploads/images/",
                          toolbars='besttome', filePath='uploads/files/')
    order = models.IntegerField('排序号', default=0)

    class Meta:
        verbose_name = u"课外阅读"
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.questions_org.__str__() + '(' + self.name + ')'


class reading_comprehension(models.Model):
    '阅读理解题库'

    '''
    填空题：开头以'F'开头，如果1个题目有多个空，则中间用'|'分割开。多个答案之间用';'分割开
    单选题：开头以'C'开头，题目与答案之间用'@'分开，选项之间则用'|'分割开
    多选题：开头以'M'开头，题目与答案之间用'@'分开，选项之间则用'|'分割开。多个答案之间用';'分割开
    '''
    questions_org = models.ForeignKey(grade_course, verbose_name=u"题目分类", on_delete=models.CASCADE)
    name = UEditorField('题目', height=300, width=1000,
                        default=u'', blank=True, imagePath="uploads/images/",
                        toolbars='besttome', filePath='uploads/files/')
    question_1 = models.TextField(max_length=300, verbose_name=u"问题1")
    answer_1 = models.CharField(max_length=300, verbose_name=u"答案1")
    question_2 = models.TextField(max_length=300, verbose_name=u"问题2", null=True, blank=True)
    answer_2 = models.CharField(max_length=300, verbose_name=u"答案2", null=True, blank=True)
    question_3 = models.TextField(max_length=300, verbose_name=u"问题3", null=True, blank=True)
    answer_3 = models.CharField(max_length=300, verbose_name=u"答案3", null=True, blank=True)
    question_4 = models.TextField(max_length=300, verbose_name=u"问题4", null=True, blank=True)
    answer_4 = models.CharField(max_length=300, verbose_name=u"答案4", null=True, blank=True)
    question_5 = models.TextField(max_length=300, verbose_name=u"问题5", null=True, blank=True)
    answer_5 = models.CharField(max_length=300, verbose_name=u"答案5", null=True, blank=True)
    question_6 = models.TextField(max_length=300, verbose_name=u"问题6", null=True, blank=True)
    answer_6 = models.CharField(max_length=300, verbose_name=u"答案6", null=True, blank=True)
    question_7 = models.TextField(max_length=300, verbose_name=u"问题7", null=True, blank=True)
    answer_7 = models.CharField(max_length=300, verbose_name=u"答案7", null=True, blank=True)
    question_8 = models.TextField(max_length=300, verbose_name=u"问题8", null=True, blank=True)
    answer_8 = models.CharField(max_length=300, verbose_name=u"答案8", null=True, blank=True)
    keypoint = models.CharField(max_length=300, verbose_name=u"知识点", null=True, blank=True)
    point = models.IntegerField(default=0, verbose_name=u'题目分值', null=True, blank=True)
    complexity = models.CharField(max_length=300, verbose_name=u"难度", null=True, blank=True)
    show_time = models.CharField(verbose_name=u"题目出现时间填写(月-日的形式：如12-18)", max_length=10, )
    add_time = models.DateTimeField(null=True, blank=True, verbose_name=u"添加时间", auto_now_add=True)
    # detail = models.CharField(verbose_name=u"试题解析", max_length=50)
    detail = UEditorField('试题解析', height=100, width=1000,
                          default=u'', blank=True, imagePath="uploads/images/",
                          toolbars='besttome', filePath='uploads/files/')
    order = models.IntegerField('排序号', default=0)

    class Meta:
        verbose_name = u"阅读理解题库"
        verbose_name_plural = verbose_name
        ordering = ['order']

    def __str__(self):
        return self.questions_org.__str__() + '(' + self.name + ')'
