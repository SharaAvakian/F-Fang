from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/', views.add_to_cart, name='cart_add'),
    path('remove/', views.remove_from_cart, name='cart_remove'),
    path('update/', views.update_cart, name='cart_update'),
]
