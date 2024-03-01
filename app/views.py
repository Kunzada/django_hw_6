from django.shortcuts import render, redirect
from .models import *

# Просмотр всех данных книг
def books(request):
    categories = Category.objects.all()
    books = Book.objects.filter(status=Book.Status.available)
    if request.GET.get('category'):
        books = books.filter(category__name=request.GET.get('category'))
        
    context = {
        'categories': categories,
        'books': books
    }
    return render(request, 'books.html', context)

# Создание книги 
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        cover = request.FILES.get('cover')
        price = request.POST.get('price')
        author = request.POST.get('author')
        description = request.POST.get('description')
        status = request.POST.get('status')
        category = Category.objects.get(id=request.POST.get('category'))
        Book.objects.create(
            title=title,
            cover=cover,
            price=price,
            author=author,
            description=description,
            status=status,
            category=category
        )
        return redirect('home')
    
    return render(request, 'create.html', {'categories': Category.objects.all(), 'statuses': Book.Status.choices})

# Просмотр книги по его ID
def book(request, book_id):
    return render(request, 'book.html', {'book': Book.objects.get(id=book_id)})

# Редактирование книги по ID
def update(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        title = request.POST.get('title', book.title)
        cover = request.FILES.get('cover', book.cover)
        price = request.POST.get('price', book.price)
        author = request.POST.get('author', book.author)
        description = request.POST.get('description', book.description)
        status = request.POST.get('status', book.status)
        category = Category.objects.get(id=request.POST.get('category', book.category.id))
        Book.objects.filter(id=book_id).update(
            title=title,
            cover=cover,
            price=price,
            author=author,
            description=description,
            status=status,
            category=category
        )
        return redirect('home')
    return render(request, 'update.html', {'book': book, 'categories': Category.objects.all(), 'statuses': Book.Status.choices})

# Удаление книги по ID
def delete(request, book_id):
    Book.objects.filter(id=book_id).delete()
    return redirect('home')