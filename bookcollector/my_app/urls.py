from django.urls import path
from .views import BookCreate, BookUpdate, BookDelete, BookList, BookDetail, home, about, book_index, book_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('books/add/', BookCreate.as_view(), name='book_create'),  # Match 'book_create'
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
    path('books/index/', book_index, name='book_index'),
    path('books/<int:book_id>/detail/', book_detail, name='book_detail'),
]
