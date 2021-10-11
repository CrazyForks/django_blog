from django.db import models
from django.utils import timezone

from utils.ModelChoices import ChoicesArticleStatus

class Category(models.Model):
    name = models.CharField('分类名', max_length=64)
    sort = models.SmallIntegerField('分类排序', default=0, help_text="数字越小，排名越靠前")
    created = models.DateTimeField(verbose_name='添加时间',  auto_now_add=True)
    modified = models.DateTimeField(verbose_name='修改时间', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:  # 按sort排序
        ordering = ['sort']

def Category_未分类():
    """如果某个分类被删除，就把该分类下的文章移入【未分类】下"""
    return Category.objects.get_or_create(username='未分类')[0]


class Article(models.Model):
    title = models.CharField('文章标题',max_length=128)
    category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.SET(Category_未分类), )
    status = models.IntegerField('文章状态', choices=ChoicesArticleStatus.choices, default=ChoicesArticleStatus.PUBLIC)
    is_original = models.BooleanField('是否原创', default=True)

    content = models.TextField('文章内容')


    keywords = models.CharField('seo的keywords', max_length=640)
    description = models.CharField('seo的description', max_length=640)

    click = models.PositiveIntegerField('点击量',default=0)

    created = models.DateTimeField(verbose_name='添加时间',  auto_now_add=True)
    modified = models.DateTimeField(verbose_name='修改时间', default=timezone.now)


