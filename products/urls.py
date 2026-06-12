from django.urls import path
from . import views

urlpatterns = [

    path('', views.product_list, name='product_list'),

    path(
        'product/<int:pk>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'add-to-cart/<int:pk>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'remove-from-cart/<int:pk>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'seller/',
        views.seller_dashboard,
        name='seller_dashboard'
    ),

    path(
        'seller/add/',
        views.add_product,
        name='add_product'
    ),

    path(
        'seller/edit/<int:pk>/',
        views.edit_product,
        name='edit_product'
    ),

    path(
        'seller/delete/<int:pk>/',
        views.delete_product,
        name='delete_product'
    ),

path(
    'seller/orders/',
    views.seller_orders,
    name='seller_orders'
),
]