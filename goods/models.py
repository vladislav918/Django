from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')


    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, verbose_name='Автор')


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)


    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


    def __str__(self):
        return self.name


class Comment(models.Model):
    context = models.TextField(verbose_name="Сообщение")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Пост")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product} - {self.user}"
