from django.contrib import admin
from .models import Authors, Articles

myModels = [Authors, Articles]

admin.site.register(myModels)