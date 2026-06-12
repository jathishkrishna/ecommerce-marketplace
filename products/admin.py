from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'seller',
        'price'
    )

    search_fields = (
        'name',
        'seller__username'
    )

    list_filter = (
        'seller',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'phone',
        'total_price',
        'created_at'
    )

    search_fields = (
        'customer_name',
        'phone'
    )

    readonly_fields = (
        'created_at',
    )

    fields = (
        'customer_name',
        'address',
        'phone',
        'total_price',
        'created_at'
    )