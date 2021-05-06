from django.contrib import admin

from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['name', 'category']
    search_fields = ('name',)
    list_editable = ['price']


admin.site.register(Category)