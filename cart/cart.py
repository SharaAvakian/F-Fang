from .models import Cart, CartItem
from products.models import Product, ProductVariant


def get_or_create_cart(request):
    """Get or create a cart for the current session/user."""
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        # Merge session cart into user cart on login
        session_key = request.session.session_key
        if session_key:
            try:
                session_cart = Cart.objects.get(session_key=session_key, user=None)
                for item in session_cart.items.all():
                    existing = cart.items.filter(product=item.product, variant=item.variant).first()
                    if existing:
                        existing.quantity += item.quantity
                        existing.save()
                    else:
                        item.cart = cart
                        item.save()
                session_cart.delete()
            except Cart.DoesNotExist:
                pass
        return cart
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart, _ = Cart.objects.get_or_create(session_key=session_key, user=None)
        return cart


def add_to_cart(request, product_id, variant_id=None, quantity=1):
    cart = get_or_create_cart(request)
    product = Product.objects.get(id=product_id)
    variant = ProductVariant.objects.get(id=variant_id) if variant_id else None

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        variant=variant,
        defaults={'quantity': quantity}
    )
    if not created:
        item.quantity += int(quantity)
        item.save()
    return item


def remove_from_cart(request, item_id):
    cart = get_or_create_cart(request)
    CartItem.objects.filter(id=item_id, cart=cart).delete()


def update_cart_item(request, item_id, quantity):
    cart = get_or_create_cart(request)
    try:
        item = CartItem.objects.get(id=item_id, cart=cart)
        if int(quantity) <= 0:
            item.delete()
        else:
            item.quantity = int(quantity)
            item.save()
    except CartItem.DoesNotExist:
        pass


def clear_cart(request):
    cart = get_or_create_cart(request)
    cart.items.all().delete()
