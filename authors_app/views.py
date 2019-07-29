from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Authors
from .forms import AuthorForm, ArticleForm


def article_list(request):
    articles = Articles.objects.all()
    authors = Authors.objects.all()
    return render(request, 'authors_app/article_list.html', context={
        'articles': articles,
        'authors': authors
    })


def article_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    authors = Authors.objects.filter(articles__id=pk)
    return render(request, 'authors_app/article_detail.html', context={
        'article': article,
        'authors': authors
    })


def article_edit(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    page_title = 'Редактирование статьи'

    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # print(article_form.cleaned_data.get("bebe"))
            article = article_form.save(commit=False)
            article.save()

            return redirect('article_detail', pk=article.pk)
    else:
        article_form = ArticleForm(instance=article)

    article = Articles.objects.get(pk=pk)
    authors_list = [d['name'] for d in (list(article.authors.values('name')))]

    return render(request, 'authors_app/article_edit.html', context={
        'article_form': article_form,
        'page_title': page_title,
        'authors_list': authors_list,
        'article': article
    })


def add_author(request):
    author_form = AuthorForm()

    return render(request, 'authors_app/article_edit.html', context={
        'author_form': author_form,
    })


def article_new(request):
    """
    Create new article
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

            article.authors.add(author)
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
    # article = get_object_or_404(Articles, pk=pk)
    article = Articles.objects.get(id=pk)
    title = article.title
    authors_inst = article.authors.filter().values('name')
    authors_list = [d['name'] for d in list(authors_inst.values('name'))]

    print(title, authors_list)
    # todo: тут можно не удалять авторов при удалении статьи
    article.delete()
    return render(request, 'authors_app/article_remove.html', context={
        'title': title,
        'authors_list': authors_list
    })


def author_list(request):
    authors = Authors.objects.all()
    return render(request, 'authors_app/author_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(Authors, pk=pk)
    return render(request, 'authors_app/author_detail.html', context={
        'author': author
    })


def author_edit(request, pk):
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
    author = Authors.objects.get(id=pk)
    name = author.name

    # if remove the author then remove all his articles
    article_list = Articles.objects.filter(authors__id=pk)
    for article in article_list:
        if article.authors.count() == 1:
            article.delete()
        else:
            author.articles.remove(article)

    author.delete()

    return render(request, 'authors_app/author_remove.html', context={
        'name': name,
    })
