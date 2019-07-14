from django.contrib import admin
from .models import Authors
from .models import Articles

myModels = [Authors, Articles]

admin.site.register(myModels)