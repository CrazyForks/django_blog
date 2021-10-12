from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,MonthArchiveView
from django.views.generic.dates import MonthArchiveView ,YearArchiveView
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.db.models import Q
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from django.urls import reverse
from .models import Article,Category


class ArticleListView(ListView):
    # model = Article
    # queryset = Article.get_public_article()
    paginate_by = 10


    def get_queryset(self):
        pk = self.kwargs.get("pk", None)
        q = self.request.GET.get('q', None)  # 搜索关键词
        if pk:
            articles = Article.get_public_article().filter(category=pk)
        else:
            articles = Article.get_public_article()

        if q:
            articles = articles.filter(Q(title__contains=q) | Q(content_markdown__contains=q))

        return articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_CONFIG'] = settings.SITE_CONFIG  # 网站配置信息
        context['category'] = Category.objects.all()  # 网站分类
        context['q'] = self.request.GET.get('q', None)  # 搜索关键词

        category_id = self.kwargs.get("pk", None)   # 分类id
        if category_id:
            # 为真表示用户传入了分类id，想要查看某个分类下的文章
            context['category_item'] = Category.objects.get(pk=category_id)


        return context


class ArticleDetailView(DetailView):
    # model = Article
    queryset = Article.get_public_article()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_CONFIG'] = settings.SITE_CONFIG  # 网站配置信息
        context['category'] = Category.objects.all()  # 网站分类
        # context['now'] = timezone.now()
        return context




class AboutPageView(TemplateView):

    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_CONFIG'] = settings.SITE_CONFIG  # 网站配置信息
        return context




class IndexPageView(ListView):
    queryset = Article.get_public_article()
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_CONFIG'] = settings.SITE_CONFIG  # 网站配置信息
        context['category'] = Category.objects.all()  # 网站分类
        return context



class RssSiteArticleFeed(Feed):
    title = settings.SITE_CONFIG.get("网站名称")
    link = "/blog/rss/"
    description = settings.SITE_CONFIG.get("网站描述")

    def items(self):
        return Article.get_public_article().order_by('-created')[:50] # 最近的50篇文章

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description


# atom，若不需要可删除
class AtomSiteArticleFeed(RssSiteArticleFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteArticleFeed.description




