from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product, Order
from .forms import ProductForm


# Home Page
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )


# Product Detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )


# Add To Cart
def add_to_cart(request, pk):
    cart = request.session.get('cart', [])

    if pk not in cart:
        cart.append(pk)

    request.session['cart'] = cart

    return redirect('cart')


# Cart
def cart(request):
    cart = request.session.get('cart', [])

    products = Product.objects.filter(
        id__in=cart
    )

    total = sum(
        product.price
        for product in products
    )

    return render(
        request,
        'products/cart.html',
        {
            'products': products,
            'total': total
        }
    )


# Remove From Cart
def remove_from_cart(request, pk):
    cart = request.session.get('cart', [])

    if pk in cart:
        cart.remove(pk)

    request.session['cart'] = cart

    return redirect('cart')


# Checkout
def checkout(request):

    if request.method == 'POST':

        cart = request.session.get('cart', [])

        products = Product.objects.filter(
            id__in=cart
        )

        total = sum(
            product.price
            for product in products
        )

        Order.objects.create(
            customer_name=request.POST['name'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            total_price=total
        )

        request.session['cart'] = []

        return render(
            request,
            'products/order_success.html'
        )

    return render(
        request,
        'products/checkout.html'
    )


# Seller Dashboard
@login_required
def seller_dashboard(request):

    products = Product.objects.filter(
        seller=request.user
    )

    return render(
        request,
        'products/seller_dashboard.html',
        {
            'products': products
        }
    )


# Add Product
@login_required
def add_product(request):

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            product = form.save(
                commit=False
            )

            product.seller = request.user

            product.save()

            return redirect(
                'seller_dashboard'
            )

    else:
        form = ProductForm()

    return render(
        request,
        'products/add_product.html',
        {
            'form': form
        }
    )
@login_required
def edit_product(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
        seller=request.user
    )

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            form.save()

            return redirect('seller_dashboard')

    else:
        form = ProductForm(
            instance=product
        )

    return render(
        request,
        'products/add_product.html',
        {'form': form}
    )


@login_required
def delete_product(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
        seller=request.user
    )

    product.delete()

    return redirect('seller_dashboard')
@login_required
def seller_orders(request):

    orders = Order.objects.filter(
        product__seller=request.user
    )

    return render(
        request,
        'products/seller_orders.html',
        {
            'orders': orders
        }
    )