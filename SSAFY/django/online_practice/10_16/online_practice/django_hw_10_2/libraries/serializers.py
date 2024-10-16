from rest_framework import serializers
from .models import Book

class BookTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'