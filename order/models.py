from django.db import models
from shared.models import TimestampMixins
from django.contrib.auth.models import User
from checkout.models import Checkout


class Order(TimestampMixins):
    PAYMENT_METHOD = [
        ('O', 'ONLINE')
    ]
    ORDER_STATUS = [
        ('PE', 'PENDING'),
        ('PA', 'PAID'),
        ('PR', 'PROCESSING'),
        ('CN', 'CANCELLED'),
        ('DE', 'DELIVERED')
    ]
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    shipping_address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHOD, default='O')
    checkout_id = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=2, choices=ORDER_STATUS, default='PE')
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order: {self.id}---Customer: {self.customer}---status: {self.status}"



class OrderItem(TimestampMixins):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variant_name = models.CharField(max_length=255)
    manufacturer_part_number = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order: {self.order_id.id}---product: {self.product_variant_name}---quantity: {self.quantity}"