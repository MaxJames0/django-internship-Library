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
    
    
class BookList(ListView):
    template_name = "./books/books.html"
    model = Book
    context_object_name = 'books'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset


class BookDetail(DetailView):
    model = Book
    template_name = 'books/detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()

        # Next book by creation date
        context['next_book'] = Book.objects.filter(
            created_at__gt=book.created_at, is_published=True
        ).order_by('created_at').first()

        # Previous book by creation date
        context['previous_book'] = Book.objects.filter(
            created_at__lt=book.created_at, is_published=True
        ).order_by('-created_at').first()

        # Latest 3 published books
        context['latest_books'] = Book.objects.filter(
            is_published=True
        ).order_by('-created_at')[:3]

        # All categories
        context['all_categories'] = BookCategory.objects.all()

        # Comment form
        context['form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = self.object     # assign the current book
            comment.user = request.user    # assign the logged-in user
            comment.save()
            return redirect("books:detail-book", pk=self.object.pk, slug=self.object.slug)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
    
