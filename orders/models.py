from django.db import models
from django.contrib.auth.models import User
from products.models import Product, ProductVariant


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('payment_confirmed', 'Payment Confirmed'),
        ('processing', 'Processing'),
        ('sent_to_pod', 'Sent to POD'),
        ('in_production', 'In Production'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('card', 'Credit/Debit Card'),
        ('arca', 'ArCa (Armenian Card)'),
        ('paypal', 'PayPal'),
        ('cod', 'Cash on Delivery'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    # Guest orders allowed
    guest_email = models.EmailField(blank=True)

    # Shipping
    shipping_name = models.CharField(max_length=200)
    shipping_email = models.EmailField()
    shipping_phone = models.CharField(max_length=30, blank=True)
    shipping_address = models.TextField()
    shipping_city = models.CharField(max_length=100)
    shipping_country = models.CharField(max_length=100)
    shipping_zip = models.CharField(max_length=20, blank=True)

    # Financials
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Payment
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD_CHOICES, default='card')
    payment_status = models.CharField(max_length=30, default='unpaid')
    payment_reference = models.CharField(max_length=200, blank=True)

    # Status & tracking
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    tracking_number = models.CharField(max_length=200, blank=True)
    tracking_url = models.URLField(blank=True)

    # POD
    pod_order_id = models.CharField(max_length=200, blank=True)
    pod_provider = models.CharField(max_length=100, blank=True)

    # Notes
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} — {self.shipping_name}"

    def save(self, *args, **kwargs):
        self.total_price = self.subtotal + self.shipping_cost
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=50, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product_name}"

    @property
    def subtotal(self):
        return self.price * self.quantity
