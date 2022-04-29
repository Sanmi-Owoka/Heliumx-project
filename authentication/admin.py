from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'roles')
    list_display_links = ('id', 'firstname', 'lastname')
    search_fields = ('firstname', 'lastname', 'email')
    list_filter = ('roles',)


admin.site.register(User, UserAdmin)
