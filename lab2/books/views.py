from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the URL name of your login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None
    return render(request, 'registration/login.html', {'error_message': error_message})



@login_required(login_url="/login/")
@permission_required('has_add_permission', raise_exception=True)
def book_list(request):
    print(1111111111111111)
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required(login_url="/login/")
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required(login_url="/login/")
def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        rate = request.POST['rate']
        views = request.POST['views']
        Book.objects.create(title=title, desc=desc, rate=rate, views=views)
        return redirect('book_list')
    return render(request, 'books/book_create.html')

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_delete.html', {'book': book})
