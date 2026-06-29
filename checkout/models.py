from django.db import models
from shared.models import TimestampMixins
from cart.models import Cart
from django.contrib.auth.models import User



class Checkout(TimestampMixins):
    # Note: Since it's a frozen snapshot of both "order" & "payment" tables, by no mean a checkout record will be deleted
    CHECKOUT_STATUS = [
        ('OP', 'OPEN'),
        ('PP', 'PAYMENT_PENDING'),
        ('CN', 'CANCELLED'),
        ('CM', 'COMPLETED'),
    ]
    PAYMENT_PROVIDER = [
        ('S', 'STRIPE')
    ]
    cart_id = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=2, choices=CHECKOUT_STATUS, default='OP')
    grand_total = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_address = models.CharField(max_length=255)
    payment_provider = models.CharField(max_length=1, choices=PAYMENT_PROVIDER, default='S')
    payment_intent_id = models.CharField(max_length=100, null=True, blank=True)
    stripe_sesison_id = models.CharField(max_length=100, null=True, blank=True)
    # SAMPLE STRUCTURE OF JSONB
    # [{'variant_id':1001, 'variant_name':'', 'brand':'', 'model_number':'', 'quantity':20, 'unit_price':15.65, 'line_total': 254.50}]
    checkout_items = models.JSONField(default=list)