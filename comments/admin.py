from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'created_at', 'likes']
    list_filter = ['created_at', 'author']
    search_fields = ['text', 'author']
