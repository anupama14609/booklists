from django.urls import path 
# from .views import BookList, book_create
from .views import book_list,book_create, book_update,book_delete
urlpatterns = [ 
    # path('', BookList, name=''),
    path('books/', book_list, name='book-list'),
    path('books/create/', book_create, name='book_create'),
    path('books/update/<pk>', book_update, name='book_update'),
    path('books/delete/<pk>', book_delete, name='book_delete'),
]


