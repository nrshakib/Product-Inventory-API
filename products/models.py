from django.db import models

from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, default="")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name