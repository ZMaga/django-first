from django.contrib import admin
from .models import Authors, Articles, AuthorArticles

myModels = [Authors, Articles, AuthorArticles]

admin.site.register(myModels)