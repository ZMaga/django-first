from django import forms
from .models import Articles, Authors, AuthorArticles


# class ArticleForm(forms.ModelForm):

#     class Meta:
#         model = Articles
#         fields = ('title', 'published_date', 'text')


# class AuthorForm(forms.ModelForm):

#     class Meta:
#         model = Authors
#         fields = ('nikname', 'name', 'birthday')



class AuthorArticlesForm(forms.ModelForm):
    
    class Meta:
        model = AuthorArticles
        exclude = ['title', 'nikname']

