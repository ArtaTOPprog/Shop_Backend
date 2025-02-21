from django.db import models
from django.contrib.auth.models import User

class Catigories(models.Model): 
    name = models.CharField(max_length=150,unique=True, verbose_name='Название') 
    slug = models.SlugField(max_length=200,unique=True, blank=True, null=True, verbose_name='URL') 
     
    class Meta: 
        db_table:str = 'category' 
        verbose_name:str = 'Категорию' 
        verbose_name_plural:str = 'Категории' 
 
    def __str__(self)->str: 
        return self.name 
 
class Product(models.Model): 
    name = models.CharField(max_length=150,unique=True, verbose_name='Название')
    brand = models.TextField(max_length=100,blank=True, null=True, verbose_name='Брэнд')
    slug = models.SlugField(max_length=200,unique=True, blank=True, null=True, verbose_name='URL')# Транслитерация продукта
    description = models.TextField(blank=True, null=True, verbose_name='Описание')  # Описание 
    price = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, verbose_name='Цена') 
    discuont = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %') 
    count = models.PositiveIntegerField(default=0, verbose_name='Количество') 
    categories = models.ForeignKey(to=Catigories, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta: 
        db_table:str = 'product' 
        verbose_name:str = 'Продукт' 
        verbose_name_plural:str = 'Продукты' 
 
    def __str__(self)->str: 
        return f'{self.name} Количество - {self.count}'