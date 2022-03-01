from django.contrib import admin
from .models import Post

# Register your models here.



@admin.action(description='Mark as published')



def make_published(modeladmin, request, queryset):
    queryset.update(status='published')

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'create_time']
    ordering = ['title']
    actions = [make_published]
admin.site.register(Post, PostAdmin)