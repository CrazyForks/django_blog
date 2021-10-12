from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,MonthArchiveView
from django.views.generic.dates import MonthArchiveView ,YearArchiveView

from django.conf import settings

from .models import Article,Category


class ArticleListView(ListView):
    # model = Article
    queryset = Article.get_public_article()
    paginate_by = 3


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_CONFIG'] = settings.SITE_CONFIG  # 网站配置信息
        context['category'] = Category.objects.all()  # 网站分类
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



class CategoryDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_CONFIG'] = settings.SITE_CONFIG  # 网站配置信息

        # context['now'] = timezone.now()
        return context






def index(request):
    return render(request=request, template_name="blog/index.html")


def about(request):
    return render(request=request,template_name="blog/about.html")




