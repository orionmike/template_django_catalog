from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "is_publish", "price", 'id')


class CategoryAdmin(MPTTModelAdmin):
    list_display = ("title", "is_publish", 'id')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ProductCategory, CategoryAdmin)


# @admin.register(ProductCategory)
# class ProductCategorykAdmin(admin.ModelAdmin):
#     list_display = ("title",  'id')
