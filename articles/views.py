from django.shortcuts import render, redirect
from . import models
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    titles, contents,pk = [], [], []
    for i in articles:
        titles.append(i.title)
        contents.append(i.content)
        pk.append(i.pk)
    context = {
        'article' : articles,
        'a' : titles,
        'b' : contents
    }
    return render(request, 'articles/index.html',context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image')
    articles = Article(title=title, content=content, image=image)
    articles.save()
    return redirect('/articles/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'pk' : article.pk,
        'title' : article.title,
        'content' : article.content,
        'created' : article.created_at,
        'updated' : article.updated_at,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    article.title = title
    content = request.POST.get('content')
    article.content = content
    article.save()
    return redirect('/articles/')

def edit(request, pk):
    articles = Article.objects.get(pk=pk)
    context = {
        'articles': articles,
    }
    return render(request,'articles/edit.html', context)