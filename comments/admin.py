from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'pub_date')
    list_filter = ('user', 'post')
    search_fields = ('user', 'post', 'pub_date')
    
admin.site.register(Comment, CommentAdmin)