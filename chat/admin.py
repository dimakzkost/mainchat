from django.contrib import admin
from .models import Message, Dialog


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'receiver', 'sender', 'created_at', 'delivered')
    list_display_links = ('id', 'text')
    search_fields = ('id', 'text')


class DialogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Message, MessageAdmin)
admin.site.register(Dialog, DialogAdmin)