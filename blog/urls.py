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
from django.views.generic.dates import ArchiveIndexView
from .models import Article
from .views import index,about
from .views import ArticleListView,ArticleDetailView,CategoryDetailView

urlpatterns = [
    path('', index, name='home'),
    path('article', ArticleListView.as_view(), name="article-list"),
    path('article/<pk>/', ArticleDetailView.as_view(), name="article-detail"),


    path('category/<pk>', CategoryDetailView.as_view(), name="category-detail"),
    path('about', about, name="about"),


]
