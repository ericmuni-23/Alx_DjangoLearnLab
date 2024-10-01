from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for publication year
    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested serialization to include related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

class BookSerializer(serializers.ModelSerializer):
   # Serializes Book fields, ensures publication_year is valid
   def validate_publication_year(self, value):
       if value > datetime.datetime.now().year:
           raise serializers.ValidationError("Publication year cannot be in the future.")
       return value

class AuthorSerializer(serializers.ModelSerializer):
   # Serializes Author and includes nested books using BookSerializer
   books = BookSerializer(many=True, read_only=True)
