from django import forms
from .models import Articles, Authors


class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Authors
        labels = {
            "name": "Введите имя автора"
        }
        fields = ['name']



class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Articles
        labels = {
            "title": "Название статьи",
            "text": "Текст статьи"
        }
        exclude = ['publications']
