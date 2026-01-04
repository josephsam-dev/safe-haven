from django.contrib import admin
from .models import Product, ProductRequest

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'available', 'created_at')
    list_filter = ('category', 'available')
    search_fields = ('name',)


@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'status', 'requested_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'product__name')
