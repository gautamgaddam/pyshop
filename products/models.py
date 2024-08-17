from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default='default-slug')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    slug = models.SlugField(unique=True, default='default-slug')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=1)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.code
