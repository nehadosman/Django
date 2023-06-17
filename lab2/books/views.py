from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        rate = request.POST['rate']
        views = request.POST['views']
        Book.objects.create(title=title, desc=desc, rate=rate, views=views)
        return redirect('book_list')
    return render(request, 'books/book_create.html')

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.rate = request.POST['rate']
        book.views = request.POST['views']
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_update.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_delete.html', {'book': book})
