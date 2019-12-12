from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article
from .form import ArticleForm
# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request, 'upload_media/index.html', {
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
    else:
        form = ArticleForm()
    return render(request, 'upload_media/post_article.html', {
        'form': form
    })
