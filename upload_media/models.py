from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255, default="")
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
