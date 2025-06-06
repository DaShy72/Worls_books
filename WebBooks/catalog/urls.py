from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AutorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', views.AutorDetailView.as_view(), name='autor-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]