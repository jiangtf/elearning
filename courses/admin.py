from django.contrib import admin
from .models import *
import xlrd


class GradeCourseAdmin(admin.ModelAdmin):
    list_display = ('grade_name', 'subject_name', 'price',)
    search_fields = ('subject_name',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class subjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class grade_course_subjectAdmin(admin.ModelAdmin):
    list_display = ('grade_course', 'subject_type', 'show_type')
    search_fields = ('grade_course', 'subject_type')


class choice_questionAdmin(admin.ModelAdmin):
    list_display = ('questions_org', 'name', 'add_time')
    search_fields = ('name',)


class reading_comprehensionAdmin(admin.ModelAdmin):
    list_display = ('questions_org', 'name')
    search_fields = ('name',)


class completion_questionAdmin(admin.ModelAdmin):
    list_display = ('questions_org', 'name', 'add_time')
    search_fields = ('name',)


class outside_readingAdmin(admin.ModelAdmin):
    list_display = ('questions_org', 'name', 'add_time')
    search_fields = ('name',)


@admin.register(Impxls)
class ImpxlsAdmin(admin.ModelAdmin):
    list_display = ('subject_type', 'remark', 'updatetime')

    def save_model(self, request, obj, form, change):
        furl = obj.fileurl.url  # 文件路径
        if obj.subject_type == 'C':  # 选择题
            Imp_Choice(furl)
        elif obj.subject_type == 'F':  # 填空题
            Imp_Fill(furl)
        elif obj.subject_type == 'K':  # 课外阅读
            Imp_OR(furl)
        else:  # 阅读理解
            pass
        super(ImpxlsAdmin, self).save_model(request, obj, form, change)


def Imp_Choice(furl):
    '单选题库导入'
    xlsfile = xlrd.open_workbook(furl)
    table = xlsfile.sheet_by_index(0)
    n_rows = table.nrows  # 行数
    for num in range(1, n_rows):
        row = table.row_values(num)
        m, created = choice_question.objects.get_or_create(questions_org_id=row[14],
                                                           name=row[1],
                                                           choice_type=row[2],
                                                           choice_A=row[3],
                                                           choice_B=row[4],
                                                           choice_C=row[5],
                                                           choice_D=row[6],
                                                           answer=row[7],
                                                           keypoint=row[8],
                                                           point=row[9],
                                                           complexity=row[10],
                                                           show_time=row[11],
                                                           detail=row[13],
                                                           order=row[14])


def Imp_Fill(furl):
    '填空题库导入'
    xlsfile = xlrd.open_workbook(furl)
    table = xlsfile.sheet_by_index(0)
    n_rows = table.nrows  # 行数
    for num in range(1, n_rows):
        row = table.row_values(num)
        m, created = completion_question.objects.get_or_create(questions_org_id=row[14],
                                                               name=row[1],
                                                               answer_1=row[2],
                                                               answer_2=row[3],
                                                               answer_3=row[4],
                                                               answer_4=row[5],
                                                               answer_5=row[6],
                                                               keypoint=row[7],
                                                               point=row[8],
                                                               complexity=row[9],
                                                               show_time=row[10],
                                                               detail=row[12],
                                                               order=row[13])


def Imp_OR(furl):
    '课外阅读题库导入'
    xlsfile = xlrd.open_workbook(furl)
    table = xlsfile.sheet_by_index(0)
    n_rows = table.nrows  # 行数
    for num in range(1, n_rows):
        row = table.row_values(num)
        m, created = outside_reading.objects.get_or_create(questions_org_id=row[9],
                                                           name=row[1],
                                                           keypoint=row[2],
                                                           point=row[3],
                                                           complexity=row[4],
                                                           show_time=row[5],
                                                           detail=row[7],
                                                           order=row[8])


admin.site.register(grade_course, GradeCourseAdmin)
admin.site.register(grade, GradeAdmin)
admin.site.register(subject, subjectAdmin)
admin.site.register(grade_course_subject, grade_course_subjectAdmin)
admin.site.register(choice_question, choice_questionAdmin)
admin.site.register(reading_comprehension, reading_comprehensionAdmin)
admin.site.register(completion_question, completion_questionAdmin)
admin.site.register(outside_reading, outside_readingAdmin)
