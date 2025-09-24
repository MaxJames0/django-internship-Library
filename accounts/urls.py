from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update_profile', ProfileUpdateView.as_view(), name='update_profile'),
    path("users/", UserListView.as_view(), name="users_list"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path('users/create/', UserCustomCreateView.as_view(), name ='user_create'),
    
]