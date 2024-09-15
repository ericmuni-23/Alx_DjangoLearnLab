from django.contrib import admin
from .models import Book
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo')

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('title', 'author')


admin.site.register(Book, BookAdmin)
