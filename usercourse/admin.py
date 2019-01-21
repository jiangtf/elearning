from django.contrib import admin
from .models import GradeCourseOrder, Choice_Question_History, Completion_Question_History, \
    Reading_Comprehension_History, Outside_Reading_History


class GradeCourseOrderAdmin(admin.ModelAdmin):
    def buy_user(self, obj):
        return obj.purchaser.nickname + '-' + obj.video_curriculum.name

    list_display = ('buy_user', 'purchaser', 'apply_bill', 'price', 'register_date')
    ordering = ('-purchaser',)


class Choice_Question_HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'choice_question', 'answer', 'answer_is_true')
    ordering = ('-add_time',)


class Completion_Question_HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'completion_question', 'answer', 'answer_is_true')
    ordering = ('-add_time',)


class Reading_Comprehension_HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'reading_comprehension', 'answer', 'answer_is_true')
    ordering = ('-add_time',)


class Outside_Reading_HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'outside_reading', 'answer', 'answer_is_true')
    ordering = ('-add_time',)


admin.site.register(GradeCourseOrder, GradeCourseOrderAdmin)
admin.site.register(Choice_Question_History, Choice_Question_HistoryAdmin)
admin.site.register(Completion_Question_History, Completion_Question_HistoryAdmin)
admin.site.register(Reading_Comprehension_History, Reading_Comprehension_HistoryAdmin)
admin.site.register(Outside_Reading_History, Outside_Reading_HistoryAdmin)
