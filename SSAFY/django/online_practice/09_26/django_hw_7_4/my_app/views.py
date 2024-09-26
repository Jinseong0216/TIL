from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    context = {
        'articles': Article.objects.all(),
    }
    return render(request, 'my_app/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('my_app:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'my_app/create.html', context)