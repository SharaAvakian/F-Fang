from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import cart as cart_module


def cart_detail(request):
    cart = cart_module.get_or_create_cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    variant_id = request.POST.get('variant_id') or None
    quantity = int(request.POST.get('quantity', 1))

    if not product_id:
        return JsonResponse({'error': 'No product specified'}, status=400)

    item = cart_module.add_to_cart(request, product_id, variant_id, quantity)
    cart = cart_module.get_or_create_cart(request)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': cart.count,
            'cart_total': str(cart.total),
            'message': f'Added {item.product.name} to cart',
        })
    return redirect('cart_detail')


@require_POST
def remove_from_cart(request):
    item_id = request.POST.get('item_id')
    cart_module.remove_from_cart(request, item_id)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        cart = cart_module.get_or_create_cart(request)
        return JsonResponse({'success': True, 'cart_count': cart.count, 'cart_total': str(cart.total)})
    return redirect('cart_detail')


@require_POST
def update_cart(request):
    item_id = request.POST.get('item_id')
    quantity = request.POST.get('quantity', 1)
    cart_module.update_cart_item(request, item_id, quantity)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        cart = cart_module.get_or_create_cart(request)
        return JsonResponse({'success': True, 'cart_count': cart.count, 'cart_total': str(cart.total)})
    return redirect('cart_detail')
