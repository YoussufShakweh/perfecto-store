from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(null=True)
    inventory = models.IntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]
