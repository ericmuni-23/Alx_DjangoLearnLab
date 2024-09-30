from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # The original list view
    path('', include(router.urls)),  # Includes all routes registered with the router
]

from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
