from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Authors
from .models import Articles
from .forms import AuthorArticlesForm


def article_list(request):
    articles = Articles.objects.all()
    return render(request, 'authors_app/article_list.html', {'articles': articles})


def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'authors_app/article_edit.html', {'form': form})


def article_edit(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'authors_app/article_edit.html', {'form': form})


def article_remove(request, pk):
    # article = get_object_or_404(Articles, pk=pk)
    article = Articles.objects.get(id=pk)
    article.delete()
    # return render(request, 'authors_app/article_remove.html', {'article': article})


def article_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    return render(request, 'authors_app/article_detail.html', {'article': article})


def authors_list(request):
    authors = Authors.objects.filter(name__contains='а')
    return render(request, 'authors_app/author_list.html', {'authors': authors})



