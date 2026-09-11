from django.contrib import admin
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
    list_filter = ('created_on', )
    date_hierarchy = 'created_on'
    search_fields = ('title', 'author')