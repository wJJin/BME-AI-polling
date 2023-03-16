from django.contrib import admin
from .models import User, PollingImage
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 
        'level',
        )
    search_fields = ('user_id',)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

class PollingImageAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 
        'user_vote',
        'name_vote'
        )
    search_fields = ('user_id',)

admin.site.register(PollingImage, PollingImageAdmin)