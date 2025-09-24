from django.urls import path, include
from .views import *

app_name = 'books'

urlpatterns = [
    path('' , BookList.as_view() , name='books-list-dashboard' ),
    path('dashboard/create', BookDashboardCreate.as_view(), name='create-book-dashboard'),
    
]
