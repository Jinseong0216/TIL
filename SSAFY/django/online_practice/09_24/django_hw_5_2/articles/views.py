from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')
