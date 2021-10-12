from django.contrib import admin
from .models import Review

# Register your models here.


class WriteReviewAdmin(admin.ModelAdmin):
    """
    Add Review admin
    """
    list_display = (
        'title',
        'comments',
        'date_created',
        'creator',
    )


admin.site.register(Review, WriteReviewAdmin)
