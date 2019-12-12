from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article, Video
from .form import ArticleForm, VideosForm
# Create your views here.


def index(request):
    return render(request, 'upload_media/index.html', {})


def list_article(request):
    articles = Article.objects.all()
    return render(request, 'upload_media/list_article.html', {
        "articles": articles
    })


def post_article(request):
    if request.POST:
        article = ArticleForm(request.POST, request.FILES)
        if article.is_valid():
            article.save()
        else:
            print(article.errors)
        return HttpResponseRedirect(reverse('upload_media:index'))

    form = ArticleForm()
    return render(request, 'upload_media/post_article.html', {
        'form': form
    })


def list_videos(request):
    videos = Video.objects.all()
    return render(request, 'upload_media/list_videos.html', {
        'videos': videos
    })


def post_videos(request):
    if request.POST:
        videos = VideosForm(request.POST, request.FILES)
        if videos.is_valid():
            videos.save()
        else:
            print(videos.errors)
        return HttpResponseRedirect(reverse("upload_media:index"))

    form = VideosForm()
    return render(request, 'upload_media/post_videos.html', {
        "form": form
    })
