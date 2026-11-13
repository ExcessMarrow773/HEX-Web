from django.contrib import admin
from encryption.models import Puzzle
# Register your models here.


@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    list_filter = ('created_on', )
    date_hierarchy = 'created_on'
    search_fields = ('name',)