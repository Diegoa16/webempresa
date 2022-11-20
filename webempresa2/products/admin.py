from django.contrib import admin
from .models import Product, Category, ProductImages

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    inlines = [ProductImagesInline]

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImages)

