from django.contrib import admin

# Register your models here.

from .models import Category,Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sort', 'name', )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title', )



