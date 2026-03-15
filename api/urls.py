from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request):
    return Response({
        'products': request.build_absolute_uri('/api/products/'),
        'categories': request.build_absolute_uri('/api/products/categories/'),
        'cart': request.build_absolute_uri('/api/cart/'),
        'orders': request.build_absolute_uri('/api/orders/'),
        'users': {
            'register': request.build_absolute_uri('/api/users/register/'),
            'token': request.build_absolute_uri('/api/users/token/'),
            'me': request.build_absolute_uri('/api/users/me/'),
        }
    })


urlpatterns = [
    path('', api_root, name='api_root'),
]
