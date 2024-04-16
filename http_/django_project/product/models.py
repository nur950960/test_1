from django.db import models

# Create your models here.

class Category(models.Model): 
    title = models.CharField(max_length=30, unique=True, verbose_name='Название')

    class Meta: 
        verbose_name='Категорию' 
        verbose_name_plural='Категории'

    def __str__(self): 
        return self.title
    
class Product(models.Model): 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')

    title = models.CharField(max_length=50, unique=True, verbose_name='Название')

    description = models.TextField(blank=True, verbose_name='Описание')

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена') 

    in_stock = models.BooleanField(default=True, verbose_name='В  наличии') 

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name='Продукт' 
        verbose_name_plural='Продукты'

    def __str__(self): 
        return f'{self.title}-{self.price}$'