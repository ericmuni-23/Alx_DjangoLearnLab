from bookshelf.models import Book

Book.objects.all().values('author', 'title', 'publication_year')
