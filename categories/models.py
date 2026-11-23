from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter=2

            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter +=1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
