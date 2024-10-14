from django.shortcuts import render, redirect
# decorators를 위함
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    review = Review.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all()
    form = ReviewForm()
    context = {
        'book': book,
        'form': form,
        'reviews': reviews,
    }
    return render(request, 'libraries/detail.html', context)


@login_required
def create_reviews(request, book_pk):
    form = ReviewForm(request.POST)
    if form.is_valid():
        # 현재 저장 할수 없으니 commit False로
        review = form.save(commit=False)
        review.user = request.user
        review.book = Book.objects.get(pk=book_pk)
        review.save()
    return redirect('libraries:detail', book_pk)


@login_required
def delete_reviews(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    book = review.book
    if request.method == "POST":
        if request.user == review.user:
            review.delete()
    return redirect('libraries:detail', book.pk)