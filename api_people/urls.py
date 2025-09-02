from django.urls import path
from .views import create_user_view

urlpatterns = [
    path('users/', create_user_view, name='create_user'),
]