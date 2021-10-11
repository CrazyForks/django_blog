from django.db import models
from django.utils import timezone
from django.urls import reverse

from utils.ModelChoices import ChoicesArticleStatus
from utils.makrdown2 import md2html_and_html_clean

class Category(models.Model):
    name = models.CharField('分类名', max_length=64)
    sort = models.SmallIntegerField('分类排序', default=0, help_text="数字越小，排名越靠前")
    created = models.DateTimeField(verbose_name='添加时间',  auto_now_add=True)
    modified = models.DateTimeField(verbose_name='修改时间', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:  # 按sort排序
        ordering = ['sort']
        verbose_name = "分类"
        verbose_name_plural = verbose_name


def category_haveNo():
    """如果某个分类被删除，就把该分类下的文章移入【未分类】下"""
    return Category.objects.get_or_create(username='未分类')[0]


class Article(models.Model):
    title = models.CharField('文章标题',max_length=128)

    category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.SET(category_haveNo), )
    # status = models.IntegerField('文章状态', choices=ChoicesArticleStatus.choices, default=ChoicesArticleStatus.PUBLIC)
    is_public = models.BooleanField('是否公开', default=True, help_text="文章是否公开展示，不勾选就对外隐藏")
    is_original = models.BooleanField('是否原创', default=True, help_text="文章是否原创，不勾选就是转载")

    content_markdown = models.TextField('文章内容markdown', null=True, blank=True)
    content_html = models.TextField('文章内容html', null=True, blank=True,help_text="返回给客户端(根据markdown自动生成的，不要手动修改)")

    keywords = models.CharField('seo的keywords', max_length=640, blank=True, null=True)
    description = models.CharField('seo的description', max_length=640, blank=True, null=True)

    click = models.PositiveIntegerField('点击量',default=0)

    created = models.DateTimeField(verbose_name='添加时间',  auto_now_add=True)
    modified = models.DateTimeField(verbose_name='修改时间', default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_public_article():
        """没有公开的文章，就不要显示出来"""
        return Article.objects.filter(is_public=True)

    # 主要是给 admin调用，在admin操作保存的时候调用
    def save(self, *args, **kwargs):
        self.content_html = md2html_and_html_clean(self.content_markdown)  # 转义危险的字符
        super().save(*args, **kwargs) # 保存


    class Meta:
        ordering = ['-created'] # 默认按照创建时间排序
        verbose_name = "文章"
        verbose_name_plural = verbose_name