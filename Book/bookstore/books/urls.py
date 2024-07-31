from django.urls import path
from .views import book_create, book_detail, book_update, book_delete, book_list

urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:pk>/', book_detail, name='book_detail'),
    path('create/', book_create, name='book_create'),
    path('<int:pk>/update/', book_update, name='book_update'),
    path('<int:pk>/delete/', book_delete, name='book_delete'),
]