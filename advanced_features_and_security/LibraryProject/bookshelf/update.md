from bookshelf.models import Book

new_book = Book.objects.filter(title='1984')

new_book.title = 'Nineteen Eighty-Four'

new_book.save()
