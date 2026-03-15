from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.CartView.as_view(), name='api_cart'),
    path('add/', api_views.AddToCartView.as_view(), name='api_cart_add'),
    path('remove/<int:item_id>/', api_views.RemoveFromCartView.as_view(), name='api_cart_remove'),
]
