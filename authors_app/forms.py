from django import forms
from .models import Articles, Authors


class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Authors
        fields = ['name']



class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Articles
        exclude = ['authors']
