from django.contrib import admin

from categories.models import CategoryModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']
    prepopulated_fields = {'slug': ('name',)}