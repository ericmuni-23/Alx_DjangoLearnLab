from bookshelf.models import Book

new_book = Book.objects.filter(title='Nineteen Eighty-Four')

new_book.delete()
