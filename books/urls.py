from django.urls import path, include
from .views import *

app_name = 'books'

urlpatterns = [
    path('', BookList.as_view(), name='list-book'),
    path('<int:pk>/<slug:slug>', BookDetail.as_view(), name='detail-book'),
    path('<int:pk>/borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('dashboard/' , BookDashboardList.as_view() , name='books-list-dashboard' ),
    path('dashboard/create', BookDashboardCreate.as_view(), name='create-book-dashboard'),
    path('dashboard/update/<int:pk>/', BookDashboardUpdate.as_view(), name='update-book-dashboard'),
    path('dashboard/delete/<int:pk>/', BookDashboardDelete.as_view(), name='delete-book'),
    path('dashboard/category/list', BookCategoryDashboardList.as_view(), name='book_category_list_dashboard'),
    path('dashboard/category/create', BookCategoryDashboardCreate.as_view(), name='book_create_category_dashboard'),
    path('dashboard/category/update/<int:pk>/', BookCategoryDashboardUpdate.as_view(), name='book_update_category_dashboard'),
    path('dashboard/category/delete/<int:pk>/', BookCategoryDashboardDelete.as_view(), name='book_delete_category_confirm_dashboard'),
    path('dashboard/borrowed-books/', BorrowedBooksDashboardView.as_view(), name='borrowed-books-dashboard'),
    path('dashboard/borrowed-books/<int:pk>/return/', ReturnBorrowedBookView.as_view(), name='return-borrowed-book'),

    
]
