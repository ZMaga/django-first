from django.conf import settings
from django.db import models
from django.utils import timezone


class Authors(models.Model):
    nikname = models.CharField(default='Some Name', max_length=50, null=False, unique=True)
    name = models.CharField(default='Some Name', max_length=100, null=False)
    birthday = models.DateField(null=False)

    def __str__(self):
        return self.name


class Articles(models.Model):
    author = models.ManyToManyField(Authors, through='AuthorArticles')
    published_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class AuthorArticles(models.Model):
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)


