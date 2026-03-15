from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from cart.cart import get_or_create_cart, clear_cart
from .models import Order, OrderItem
from .pod import dispatch_order_to_pod


def checkout(request):
    cart = get_or_create_cart(request)
    if not cart.items.exists():
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart_detail')

    if request.method == 'POST':
        # Gather form data
        data = request.POST
        errors = {}

        required = ['shipping_name', 'shipping_email', 'shipping_address', 'shipping_city', 'shipping_country']
        for field in required:
            if not data.get(field, '').strip():
                errors[field] = 'This field is required.'

        if errors:
            return render(request, 'orders/checkout.html', {
                'cart': cart,
                'errors': errors,
                'form_data': data,
            })

        # Calculate shipping (flat rate for now)
        subtotal = cart.total
        shipping_cost = 0 if subtotal >= 50 else 9.99

        # Create order
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            guest_email=data.get('shipping_email') if not request.user.is_authenticated else '',
            shipping_name=data.get('shipping_name'),
            shipping_email=data.get('shipping_email'),
            shipping_phone=data.get('shipping_phone', ''),
            shipping_address=data.get('shipping_address'),
            shipping_city=data.get('shipping_city'),
            shipping_country=data.get('shipping_country'),
            shipping_zip=data.get('shipping_zip', ''),
            subtotal=subtotal,
            shipping_cost=shipping_cost,
            payment_method=data.get('payment_method', 'card'),
            notes=data.get('notes', ''),
        )

        # Create order items from cart
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                variant=item.variant,
                product_name=item.product.name,
                product_sku=item.variant.sku if item.variant else '',
                size=item.variant.size if item.variant else '',
                color=item.variant.color if item.variant else '',
                quantity=item.quantity,
                price=item.product.price,
            )

        # Simulate payment confirmation (real gateway integration goes here)
        order.payment_status = 'paid'
        order.status = 'payment_confirmed'
        order.save()

        # Dispatch to POD
        dispatch_order_to_pod(order)

        # Clear cart
        clear_cart(request)

        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'orders/checkout.html', {'cart': cart})


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # Security: only owner or guest can see
    if order.user and request.user.is_authenticated and order.user != request.user:
        return redirect('home')
    return render(request, 'orders/confirmation.html', {'order': order})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})
