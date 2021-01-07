from django.contrib import admin
from .models import ExamCardDetails, StudentEnroll, SchoolEnroll, DictationAudio, TestSchedule ,StudentTestStats, TeluguLevels
# Register your models here.

admin.site.register(TeluguLevels)
admin.site.register(ExamCardDetails)
admin.site.register(StudentEnroll)
admin.site.register(SchoolEnroll)
admin.site.register(DictationAudio)
admin.site.register(TestSchedule)
admin.site.register(StudentTestStats)

