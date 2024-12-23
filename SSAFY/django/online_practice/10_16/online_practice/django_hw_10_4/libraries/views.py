from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Book
from .serializers import BookListSerializer, BookSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사 통과 실패의 경우
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        print('겟요청!!')
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        context = {
            'delete': f'도서 고유번호 {book.isbn}번의 {book.title}을 삭제하였습니다.',
        }
        print(context)
        book.delete()
        return Response(context, status=status.HTTP_204_NO_CONTENT)
