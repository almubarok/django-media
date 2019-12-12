from django import forms
from .models import Article, Video


class ArticleForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Article
        fields = '__all__'


class VideosForm(forms.ModelForm):
    video = forms.FileField()

    class Meta:
        model = Video
        fields = '__all__'
