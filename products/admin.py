from django.contrib import admin
from .models import Product, Offer, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
  list_display= ('name', 'price', 'stock')
  
admin.site.register(Product, ProductAdmin)


class OfferAdmin(admin.ModelAdmin):
  list_display=('code', 'discount')
  
admin.site.register(Offer, OfferAdmin)


class CategoryAdmin(admin.ModelAdmin):
  list_display=('name', 'slug')

admin.site.register(Category, CategoryAdmin)