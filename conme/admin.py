from django.contrib.admin import *
from .models import ContactMessage
@register(ContactMessage)
class FacultyAdmin(ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
