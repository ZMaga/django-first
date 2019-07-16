from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/new/', views.article_new, name='article_new'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/remove/', views.article_remove, name='article_remove'),
]

