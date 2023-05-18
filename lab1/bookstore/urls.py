from django.urls import path, include
from .views import index,bookstore_list,bookstore_details,bookstore_delete,bookstore_update,create_new_book
app_name = 'bookstore'
urlpatterns = [
    path('', index, name='bookstore-index'),
    path('bookstore-list/', index, name="bookstore-list"),
    path('bookstore_details/<int:book_id>', bookstore_details, name="bookstore-details"),
    path('book_delete/<int:book_id>', bookstore_delete, name="bookstore-delete"),
    path('book_update/<int:book_id>', bookstore_update, name="bookstore-update"),
    path('book_create/', create_new_book, name="bookstore-create"),
]