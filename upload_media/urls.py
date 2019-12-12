from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "upload_media"
urlpatterns = [
    path('', views.index, name="index"),
    path('post-article', views.post_article, name="post_article")
]
