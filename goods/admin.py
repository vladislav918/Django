from django.contrib import admin
from .models import Product, Category, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    readonly_fields= ('article_number',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
