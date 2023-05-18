from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    my_context = {'books_list': bookstore_list}
    return render(request, 'bookstore_list.html',context=my_context)

bookstore_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'book 1',
        'price': 100,
        'description': "Learning ekgjekgjgekjgek",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'book 2',
        'price': 200,
        'description': "LearningJS fffjkdfjd klgjkdgjdkgjdkgjdkgjd kgjdglkjdgk ljfj fjejekgjekgjekbgjekgjgekjgek",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'book 3',
        'price': 300,
        'description': "LearningJS fffjk dfjdklgjkdg jdkgjdkgjd kgjdkgjdglkjdgkl jfjfjejekg jekgjekgjekgjgekjgek",
    },
]


def _get_book(book_id):
    for book in bookstore_list:
        if 'id' in book and book['id'] == book_id:
            return book
    return None

def bookstore_details(request, *args, **kwrgs):
    book_id = kwrgs.get('book_id')
    book_object = _get_book(book_id)
    my_context = {
        'book_id': book_object.get('id'),
        'book_name': book_object.get('name'),
        'book_price': book_object.get('price'),
        'book_description': book_object.get('description')
    }

    return render(request, 'bookstore_details.html', context=my_context)

def bookstore_delete(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    if bookstore_list:
        bookstore_list.remove(book_object)
    return redirect('bookstore:bookstore-list')   

def bookstore_update(request, **kwargs):
    book_id = kwargs.get('book_id')
    book_object = _get_book(book_id)
    for book in bookstore_list:
        if book == book_object:
            book['name'] = f"Update {book_object['name']}"
            
    return redirect('bookstore:bookstore-list') 

def create_new_book(request):
    new_index = max(book['index'] for book in bookstore_list) + 1
    new_book = {
        'index': new_index,
        'id': new_index + 1,
        'name':"book" + str(new_index),
        'price': 3000,
        'description': "Book description",
    }
    
    # Add the new task to the task list
    bookstore_list.append(new_book)
    return redirect('bookstore:bookstore-list')