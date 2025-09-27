from pyexpat import model
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect 

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
        queryset = super().get_queryset().filter(is_published=True).order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(desc__icontains=query)
            )
        return queryset



class BookDetail(DetailView):
    model = Book
    template_name = 'books/detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()

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
    
    
class BorrowBookView(LoginRequiredMixin, View):
    login_url = 'accounts/login/'  # redirect here if not logged in

    def post(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)

        if book.is_borrowed:
            messages.error(request, "Sorry, this book is already borrowed by another user.")
        else:
            Borrow.objects.create(book=book, user=request.user)
            messages.success(request, "You have successfully borrowed this book.")

        return redirect('books:detail-book', pk=book.pk, slug=book.slug)
    
    
class BorrowedBooksDashboardView(LoginRequiredMixin, ListView):
    model = Borrow
    template_name = 'books/borrowed_books_dashboard.html'
    context_object_name = 'borrows'
    ordering = ['-borrowed_at']

    def get_queryset(self):
        qs = super().get_queryset().filter(returned=False)
        order = self.request.GET.get('order', 'asc')  # default ascending
        if order == 'desc':
            qs = qs.order_by('-borrowed_at')
        else:
            qs = qs.order_by('borrowed_at')
        return qs
    

class ReturnBorrowedBookView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        borrow = get_object_or_404(Borrow, pk=pk, returned=False)
        borrow.returned = True
        borrow.save()
        return redirect('books:borrowed-books-dashboard')