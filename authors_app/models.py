from django.utils import timezone
from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=200, null=False)
    text = models.TextField(null=False)
    publications = models.ManyToManyField(Authors, through='Publication')

    def __str__(self):
        return self.title


class Publication(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

    # publication_date = models.DateTimeField(auto_now_add=True, null=True)
    # publication_date = models.DateTimeField(default=timezone.now, null=True)

