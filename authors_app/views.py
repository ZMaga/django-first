from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Articles, Authors, Publication
from .forms import AuthorForm, ArticleForm

from rest_framework import viewsets
from .serializers import ArticlesSerializer, AuthorsSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Articles.objects.all().order_by('-title')
    serializer_class = ArticlesSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer


def article_list(request):
    """
    Список статей
    """

    articles = Articles.objects.all()
    return render(request, 'authors_app/article_list.html', context={
        'articles': articles,
    })


def article_sort_by_authors(request):
    """
    Сортировка статей по количеству авторов (от большего количества к меньшему)
    """

    articles = Articles.objects.annotate(Count('publications')).order_by("publications__count").reverse()
    return render(request, 'authors_app/article_list.html', context={
        'articles': articles,
    })


def article_sort_by_authors_reverse(request):
    """
    Сортировка статей по количеству авторов (от меньшего количества к большему)
    """

    articles = Articles.objects.annotate(Count('publications')).order_by("publications__count")

    return render(request, 'authors_app/article_list.html', context={
        'articles': articles,
    })


def article_detail(request, pk):
    """
    Детальная информация о статье
    """

    article = get_object_or_404(Articles, pk=pk)
    authors = Authors.objects.filter(articles__id=pk)
    return render(request, 'authors_app/article_detail.html', context={
        'article': article,
        'authors': authors
    })


def article_edit(request, pk):
    """
    Редактирование статьи
    """

    article = get_object_or_404(Articles, pk=pk)
    page_title = 'Редактирование статьи'

    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        author_form = AuthorForm(request.POST)

        if article_form.is_valid() and author_form.is_valid():
            article.save()
            author = author_form.save(commit=False)

            # add for article if the author is registred
            if Authors.objects.filter(name=author.name):
                author = Authors.objects.get(name=author.name)
                Publication.objects.create(author=author, article=article)

            return redirect('article_detail', pk=article.pk)
    else:
        article_form = ArticleForm(instance=article)
        author_form = AuthorForm()
        author_form.fields['name'].label = "Добавить автора"

    article = Articles.objects.get(pk=pk)
    authors_list = [d['name'] for d in (list(article.publications.values('name')))]

    return render(request, 'authors_app/article_edit.html', context={
        'article_form': article_form,
        'author_form': author_form,
        'page_title': page_title,
        'authors_list': authors_list,
        'article': article
    })


def article_new(request):
    """
    Создание новой статьи
    """
    page_title = 'Создание новой статьи'

    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        author_form = AuthorForm(request.POST)

        if article_form.is_valid() and author_form.is_valid():
            author = author_form.save(commit=False)

            # if the author exists with this name, don't create
            if not Authors.objects.filter(name=author.name):
                author = author_form.save()
            else:
                author = Authors.objects.get(name=author.name)

            article = article_form.save(commit=False)
            # if the article exists with this title, don't create
            if not Articles.objects.filter(title=article.title):
                article = article_form.save()
            else:
                article = Articles.objects.get(title=article.title)

            Publication.objects.create(author=author, article=article)
            return redirect('article_detail', pk=article.pk)
    else:
        author_form = AuthorForm()
        article_form = ArticleForm()

    return render(request, 'authors_app/article_edit.html', context={
        'article_form': article_form,
        'author_form': author_form,
        'page_title': page_title,
    })


def article_remove(request, pk):
    """
    Удаление статьи
    """
    # article = get_object_or_404(Articles, pk=pk)
    article = Articles.objects.get(id=pk)
    title = article.title
    authors_inst = article.publications.filter().values('name')
    authors_list = [d['name'] for d in list(authors_inst.values('name'))]

    print(title, authors_list)

    article.delete()
    return render(request, 'authors_app/article_remove.html', context={
        'title': title,
        'authors_list': authors_list
    })


def author_list(request):
    """
    Список авторов
    """

    authors = Authors.objects.all()
    return render(request, 'authors_app/author_list.html', context={'authors': authors})


def author_sort_by_articles(request):
    """
    Сортировка авторов по количеству статей от большего количества к меньшему
    """

    authors = Authors.objects.annotate(Count('articles')).\
        order_by("articles__count").reverse()
    return render(request, 'authors_app/author_list.html', context={'authors': authors})


def author_sort_by_articles_reverse(request):
    """
    Сортировка авторов по количеству статей от меньшего количества к большему
    """

    authors = Authors.objects.annotate(Count('articles')).\
        order_by("articles__count")
    return render(request, 'authors_app/author_list.html', context={'authors': authors})


def author_detail(request, pk):
    """
    Детальная информация об авторе
    """

    author = get_object_or_404(Authors, pk=pk)
    return render(request, 'authors_app/author_detail.html', context={
        'author': author
    })


def author_new(request):
    """
    Добавление нового автора
    """

    page_title = 'Регистрация автора'

    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_inst = author_form.save(commit=False)

            # if the author exists with this name, don't create
            if not Authors.objects.filter(name=author_inst.name):
                author = author_form.save()
            else:
                author = Authors.objects.get(name=author_inst.name)

            return redirect('author_detail', pk=author.pk)
    else:
        author_form = AuthorForm()

    return render(request, 'authors_app/author_edit.html', context={
        'author_form': author_form,
        'page_title': page_title,
    })


def author_edit(request, pk):
    """
    Редактирование информации об авторе
    """

    author = get_object_or_404(Authors, pk=pk)
    page_title = 'Редактирование автора'

    if request.method == "POST":
        author_form = AuthorForm(request.POST, instance=author)
        if author_form.is_valid():
            author.save()
            return redirect('author_detail', pk=author.pk)
    else:
        author_form = AuthorForm(instance=author)

    return render(request, 'authors_app/author_edit.html', context={
        'author_form': author_form,
        'page_title': page_title,
    })


def author_remove(request, pk):
    """
    Удаление автора (всех его личных статей, удаление из других статей как соавтора)
    """

    author = Authors.objects.get(id=pk)
    name = author.name

    for publication in Publication.objects.filter(article_id=author.id):
        publication.remove(author)

    author_articles = Articles.objects.annotate(Count('publication__author_id')).filter(publication__author_id=pk)
    # single author
    for article in author_articles.filter(publication__author_id__count=1):
        article_inst = Articles.objects.get(id=article.id)
        print('single')
        article_inst.delete()

    author.delete()

    return render(request, 'authors_app/author_remove.html', context={
        'name': name,
    })
