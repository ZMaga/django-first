from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('authors/<int:pk>/remove/', views.author_remove, name='author_remove'),
    path('articles/new/', views.article_new, name='article_new'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('articles/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('articles/<int:pk>/remove/', views.article_remove, name='article_remove'),
]

