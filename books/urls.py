from django.urls import path, include
from .views import *

app_name = 'books'

urlpatterns = [
    path('' , BookDashboardList.as_view() , name='books-list-dashboard' ),
    path('dashboard/create', BookDashboardCreate.as_view(), name='create-book-dashboard'),
    path('dashboard/update/<int:pk>/', BookDashboardUpdate.as_view(), name='update-book-dashboard'),
    path('dashboard/delete/<int:pk>/', BookDashboardDelete.as_view(), name='delete-book'),
    
]
