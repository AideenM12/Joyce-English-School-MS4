from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    """ Course Admin """
    list_display = (
        'name',
        'description',
        'price',
        'image',
        'start_date',
        'end_date',
        'hours',
    )

    ordering = ('pk',)


admin.site.register(Course, CourseAdmin)
