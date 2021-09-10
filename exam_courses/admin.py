from django.contrib import admin
from .models import ExamCourse


class ExamCourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'required_level',
        'certification_awarded',
        'description',
        'price',
        'image',
        'start_date',
        'end_date',
        'hours',
    )

    ordering = ('pk',)


admin.site.register(ExamCourse, ExamCourseAdmin)
