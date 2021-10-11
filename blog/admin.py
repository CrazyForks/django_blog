from django.contrib import admin

# Register your models here.

from .models import Category,Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sort', 'name',  'created',  'modified', )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'category', 'status', 'is_original', 'click',  'created',  'modified', )
    list_filter = ('status', 'is_original', 'category',)
    search_fields = ('title', 'content')




