from django.contrib import admin
from .models import Newletter, Session, Subscription


class NewletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    list_display_links = ('id', 'user')
    search_fields = ('user',)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id', 'type')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor_email', 'patient_email')
    list_display_links = ('id',)


admin.site.register(Newletter, NewletterAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
