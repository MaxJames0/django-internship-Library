from pyexpat import model
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from books.forms import *
from books.models import *

# Create your views here.


class BookDashboardList(ListView):
    template_name = "books/books_list_dashboard.html"
    model = Book
    context_object_name = 'books'

    
class BookDashboardCreate(CreateView):
    template_name = 'books/book_create_dashboard.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books-list-dashboard')
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
    

class BookDashboardUpdate(UpdateView):
    template_name = "books/book_update_dashboard.html"
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books-list-dashboard')

    def form_valid(self, form):
        # keep the existing added_by user or update if you want
        if not form.instance.added_by:
            form.instance.added_by = self.request.user
        return super().form_valid(form)
    
    def form_valid(self, form):
        print("Form submitted")
        return super().form_valid(form)
    

class BookDashboardDelete(DeleteView):
    template_name = "books/book_delete_confirm_dashboard.html"
    model = Book
    success_url = reverse_lazy('books:books-list-dashboard')
    

class BookCategoryDashboardList(ListView):
    template_name = 'books/book_category_list_dashboard.html'
    model = BookCategory
    context_object_name = 'book_categories'


class BookCategoryDashboardCreate(CreateView):
    template_name = 'books/book_create_category_dashboard.html'
    model = BookCategory
    form_class = BookCategoryForm
    success_url = reverse_lazy('books:book_category_list_dashboard')
    

class BookCategoryDashboardUpdate(UpdateView):
    template_name = "books/book_update_category_dashboard.html"
    model = BookCategory
    form_class = BookCategoryForm
    success_url = reverse_lazy('books:book_category_list_dashboard')
    

class BookCategoryDashboardDelete(DeleteView):
    template_name = "books/book_delete_category_confirm_dashboard.html"
    model = BookCategory
    success_url = reverse_lazy('books:book_category_list_dashboard')


