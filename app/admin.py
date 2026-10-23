from django.contrib import admin
from app.models import Link

# Register your models here.

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_on')
    list_filter = ('created_on', )
    date_hierarchy = 'created_on'
    search_fields = ('name', 'created_by')