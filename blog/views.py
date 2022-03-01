from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Post
# Create your views here.


def sampleView(request):
    context = {
    }
    return render(request=request, template_name="base.html", context=context)


def homeView(request):
    # published_posts = Post.objects.all()
    published_posts = Post.objects.filter(status="published")
    context = {
        "posts": published_posts
    }
    return render(request=request, template_name="mood.html", context=context)



def index_blog(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request=request,template_name="index.html", context=context)

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request=request,template_name="post_details.html", context=context)