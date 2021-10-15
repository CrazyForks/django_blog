from django.contrib import admin
from reversion.admin import VersionAdmin

# Register your models here.

from .models import Category,Article

@admin.register(Category)
class CategoryAdmin(VersionAdmin):
    list_display = ('id','name',  'sort',  'created',  'modified', )
    list_display_links = ('id', 'name',)

@admin.register(Article)
class ArticleAdmin(VersionAdmin):
    list_display = ('id', 'title',  'sort',  'category', 'is_public', 'is_original', 'click',  'created',  'modified', )
    list_filter = ('is_public', 'is_original', 'category',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content_markdown')




