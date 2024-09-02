from django.views.generic import DetailView
from django.shortcuts import render
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render (request, 'book_templates/list_books.html',{'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'book_templates/library_detail.html'
    context_object_name = 'library'
