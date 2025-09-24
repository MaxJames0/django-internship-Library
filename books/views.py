from pyexpat import model
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from books.forms import *
from books.models import *

# Create your views here.


class BookList(ListView):
    template_name = "books/books_list_dashboard.html"
    model = Book
    context_object_name = 'books'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains = query) | queryset.filter(content__icontains = query)
        return queryset
    
    
class BookDashboardCreate(CreateView):
    template_name = 'books/book_create_dashboard.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books-list-dashboard')
    
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)