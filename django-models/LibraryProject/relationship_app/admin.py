from django.contrib import admin
from .models import Author, Book, Library, Librarian
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('books',)

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')

# Register the models with the custom admin classes
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Librarian, LibrarianAdmin)
