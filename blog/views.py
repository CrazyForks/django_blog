from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,MonthArchiveView
from django.views.generic.dates import MonthArchiveView ,YearArchiveView


from .models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "created"
    # make_object_list = True
    allow_future = True


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "created"
    # make_object_list = True
    allow_future = True


def index(request):
    return render(request=request, template_name="blog/index.html")


def about(request):
    return render(request=request,template_name="blog/about.html")




