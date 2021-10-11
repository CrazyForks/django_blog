from django.db import models
from django.utils import timezone
from utils.User import User
from utils.ModelChoices import ChoicesArticleStatus

class Category(models.Model):
    name = models.CharField('分类名', max_length=64)
    sort = models.SmallIntegerField('分类排序', default=0, help_text="数字越小，越靠前")
    created = models.DateTimeField(verbose_name='添加时间',  auto_now_add=True)
    modified = models.DateTimeField(verbose_name='修改时间', default=timezone.now)

    def __str__(self):
        return f'{self.name}<{self.sort}>'

    class Meta:  # 按sort排序
        ordering = ['sort']


class Article(models.Model):
    status =models.IntegerField('文章状态', choices=ChoicesArticleStatus.choices, default=ChoicesArticleStatus.PUBLIC)
    title = models.CharField('文章标题',max_length=128)
    content = models.TextField('文章内容')

    keywords = models.CharField('seo的keywords', max_length=640)
    description = models.CharField('seo的description', max_length=640)

    click = models.PositiveIntegerField('点击量',default=0)

    created = models.DateTimeField(verbose_name='添加时间',  auto_now_add=True)
    modified = models.DateTimeField(verbose_name='修改时间', default=timezone.now)


