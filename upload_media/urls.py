from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "upload_media"
urlpatterns = [
    path('', views.index, name="index"),
    path('list-article', views.list_article, name="list_article"),
    path('post-article', views.post_article, name="post_article"),
    path('list-videos', views.list_videos, name="list_videos"),
    path('post-videos', views.post_videos, name="post_videos"),
    path('list-musics', views.list_musics, name="list_musics"),
    path('post-musics', views.post_musics, name="post_musics"),
]
