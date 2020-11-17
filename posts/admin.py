from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'pub_date')
    list_filter = ('user', 'title')
    search_fields = ('user', 'title', 'pub_date')
    

admin.site.register(Post, PostAdmin)