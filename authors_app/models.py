from django.conf import settings
from django.db import models
from django.utils import timezone


class Authors(models.Model):
    name = models.CharField(default='Some Name', max_length=50, null=False, unique=True)
    birthday = models.DateField(null=False)

    def __str__(self):
        return self.name


class ArticleAuthor(models.Model):
    author_id = models.ForeignKey('Authors', on_delete=models.CASCADE)
    article_id = models.ForeignKey('Articles', on_delete=models.CASCADE)
#     # TODO: It is need the cascase removing if deleteauthor and he has the article with single author


class Articles(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    authors = models.ManyToManyField(Authors, through='ArticleAuthor')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
