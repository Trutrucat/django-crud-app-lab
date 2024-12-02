from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'read']
    template_name = 'book_create.html'  # Matches 'book_create.html'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.pk})

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'read']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

class BookList(ListView):
    model = Book
    template_name = 'book_list.html'

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

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


