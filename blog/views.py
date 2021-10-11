from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request=request,template_name="blog/index.html")


def list(request):
    return render(request=request,template_name="blog/list.html")


def detail(request):
    return render(request=request,template_name="blog/detail.html")


def about(request):
    return render(request=request,template_name="blog/about.html")



def archive(request):
    return render(request=request,template_name="blog/archive.html")

