from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    book = Book.objects.all()
    context = {
        'book': book,
    }
    return render(request, 'libraries/index.html', context)