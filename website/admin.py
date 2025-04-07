from django.contrib import admin
from website.models import ContactMessage

# Register your models here.
admin.site.register(ContactMessage)

from django.contrib import admin
from .models import Feedback  # Импортируем модель

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
