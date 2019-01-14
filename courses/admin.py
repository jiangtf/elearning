from django.contrib import admin

from .models import *


class GradeCourseAdmin(admin.ModelAdmin):
    list_display = ('grade_name', 'subject_name', 'price',)
    search_fields = ('subject_name', )


class GradeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class subjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class choice_questionAdmin(admin.ModelAdmin):
    list_display = ('questions_org', 'desc')
    search_fields = ('desc',)


class reading_comprehensionAdmin(admin.ModelAdmin):
    list_display = ('questions_org', 'desc')
    search_fields = ('desc',)

class completion_questionAdmin(admin.ModelAdmin):
    list_display = ('questions_org', 'desc')
    search_fields = ( 'desc',)

class outside_readingAdmin(admin.ModelAdmin):
    list_display = ('questions_org', 'desc')
    search_fields = ( 'desc',)

admin.site.register(grade_course, GradeCourseAdmin)
admin.site.register(grade, GradeAdmin)
admin.site.register(subject, subjectAdmin)
admin.site.register(choice_question, choice_questionAdmin)
admin.site.register(reading_comprehension, reading_comprehensionAdmin)
admin.site.register(completion_question, completion_questionAdmin)
admin.site.register(outside_reading, outside_readingAdmin)

