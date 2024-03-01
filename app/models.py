from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
class Book(models.Model):
    class Status(models.TextChoices):
        available = 'av', 'В наличии'
        not_available = 'nv', 'Нет в наличии'
    
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/', default='covers/default.jpg')
    price = models.IntegerField()
    author = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, 
                              default=Status.available)
    
    
    def get_first_category():
        return Category.objects.first()
    
    category = models.ForeignKey(Category, on_delete=models.SET(get_first_category), default=get_first_category)
    
    def __str__(self):
        return f"{self.title} ({self.author}) - {self.price}"
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'