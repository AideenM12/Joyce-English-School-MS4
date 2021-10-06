from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number',
        'postcode',
        'town_or_city', 
        'street_address1', 
        'street_address2', 
    )


admin.site.register(UserProfile)
