"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .models import Article
from .views import ArticleListView,ArticleDetailView,AboutPageView,IndexPageView,RssSiteArticleFeed,AtomSiteArticleFeed

sitemap_info_dict = {
    'queryset': Article.objects.all(),
    'date_field': 'created',
}


urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('blog', ArticleListView.as_view(), name="article-list"),
    path('blog/<pk>/', ArticleListView.as_view(), name="category-detail"),

    path('article/<pk>/', ArticleDetailView.as_view(), name="article-detail"),

    path('about', AboutPageView.as_view(), name="about"),

    # 同时支持 rss和atom，你可根据需要自己修改，默认用rss
    path('blog/rss', RssSiteArticleFeed(), name="rss"),
    # path('blog/atom', AtomSiteArticleFeed(), name="atom"),

    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(sitemap_info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),

]
