from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['subtotal']
    fields = ['product_name', 'product_sku', 'size', 'color', 'quantity', 'price', 'subtotal']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'shipping_name', 'shipping_email', 'total_price', 'status', 'payment_status', 'created_at']
    list_filter = ['status', 'payment_status', 'payment_method', 'created_at']
    list_editable = ['status']
    search_fields = ['shipping_name', 'shipping_email', 'id', 'tracking_number']
    readonly_fields = ['subtotal', 'total_price', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
    fieldsets = (
        ('Customer', {'fields': ('user', 'guest_email')}),
        ('Shipping', {'fields': ('shipping_name', 'shipping_email', 'shipping_phone', 'shipping_address', 'shipping_city', 'shipping_country', 'shipping_zip')}),
        ('Financials', {'fields': ('subtotal', 'shipping_cost', 'total_price')}),
        ('Payment', {'fields': ('payment_method', 'payment_status', 'payment_reference')}),
        ('Status & Tracking', {'fields': ('status', 'tracking_number', 'tracking_url')}),
        ('POD', {'fields': ('pod_order_id', 'pod_provider'), 'classes': ('collapse',)}),
        ('Notes', {'fields': ('notes',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
