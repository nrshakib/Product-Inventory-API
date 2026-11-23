from django.contrib import admin

from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description', 'category', 'price', 'stock_quantity', 'created_at']
    search_fields = ['name']
    list_filter = ['category', 'created_at']
    prepopulated_fields = {'slug': ('name',)}