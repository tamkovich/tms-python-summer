from django.contrib import admin

from profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = 'user', 'avatar',
    search_fields = 'user',
    list_display = 'user', 'user_profile', 'avatar', 'id',
    list_filter = 'user',


admin.site.register(Profile, ProfileAdmin)
