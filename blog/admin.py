from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'category', 'is_published', 'created_at')
	list_filter = ('category', 'is_published')
	search_fields = ('title', 'author')
	ordering = ('-created_at',)

# Register your models here.
