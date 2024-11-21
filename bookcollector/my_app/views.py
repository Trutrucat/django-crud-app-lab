from django.shortcuts import render
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'read']

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'read']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})


