from django.contrib import admin
from .models import Category, Post, Comment



class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'wathed', 'is_published', 'category')
    list_display_links = ('id', 'title')
    list_editable = ['is_published']
    readonly_fields = ['wathed']
    list_filter = ('is_published','category', 'wathed',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
