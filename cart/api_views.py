from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .cart import get_or_create_cart, add_to_cart, remove_from_cart
from .models import CartItem
from .serializers import CartSerializer


class CartView(APIView):
    def get(self, request):
        cart = get_or_create_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        variant_id = request.data.get('variant_id')
        quantity = int(request.data.get('quantity', 1))
        try:
            item = add_to_cart(request, product_id, variant_id, quantity)
            cart = get_or_create_cart(request)
            return Response({'success': True, 'cart_count': cart.count})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromCartView(APIView):
    def delete(self, request, item_id):
        remove_from_cart(request, item_id)
        return Response({'success': True})
