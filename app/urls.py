from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='home'),
    path('create/', create, name='create'),
    path('book/<int:book_id>/', book, name='book'),
    path('update/<int:book_id>/', update, name='update'),
    path('delete/<int:book_id>/', delete, name='delete'),
]
