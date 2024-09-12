# relationship_app/urls.py

from django.urls import path
from .views import books_list, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import view
from django.urls import path
from .admin_view import Admin
from .librarian_view import Librarian
from .member_view import Member

urlpatterns = [
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', Admin.as_view(), name='admin_view'),
    path('librarian/', Librarian.as_view(), name='librarian_view'),
    path('member/', Member.as_view(), name='member_view'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]

'''
urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),]
'''
'''
urlpatterns = [
    path('admin/', Admin.as_view(), name='admin_view'),
    path('librarian/', Librarian.as_view(), name='librarian_view'),
    path('member/', Member.as_view(), name='member_view'),
]
'''
