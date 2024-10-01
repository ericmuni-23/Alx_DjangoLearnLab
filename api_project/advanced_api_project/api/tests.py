from django.test import TestCase

# Create your tests here.
from api.models import Author, Book
from api.serializers import AuthorSerializer

author = Author.objects.create(name="George Orwell")
book = Book.objects.create(title="1984", publication_year=1949, author=author)

author_serializer = AuthorSerializer(author)
print(author_serializer.data)
