from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
# import logging

# Create your views here.


def homepage(request):
    if request.method == "POST":
        search_query = request.POST['search']
        print(search_query,"dadtaat")
        books = Book.objects.filter(title__icontains=search_query) | Book.objects.filter(author__icontains=search_query)
    else:
        books = Book.objects.all()
    return render(request, 'templates/homepage.html', {'books': books})

def search_books(request):
    search_query = request.POST['search']
    books = Book.objects.filter(title__icontains=search_query) | Book.objects.filter(author__icontains=search_query)
    return render(request, 'templates/homepage.html', {'books': books})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'templates/book_list.html', {'books': books})

def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'templates/book_details.html', {'book': book})

def add_book(request):
    if request.method == "POST":

        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm()
    return render(request, 'templates/add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_details', book_id)
        else:
            print("formerrors",form.errors)
    else:
        form = BookForm(instance=book)
    return render(request, 'templates/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('homepage')
    return render(request, 'templates/delete_book.html', {'book': book})

