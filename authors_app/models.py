from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=200, null=False)
    # TODO: set not null
    text = models.TextField()
    authors = models.ManyToManyField(Authors, related_name='articles')

    def __str__(self):
        return self.title
