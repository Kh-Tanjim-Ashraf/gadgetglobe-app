from django.db import models
from shared.models import TimestampMixins
from django.contrib.auth.models import User
from product.models import ProductVariant


class Cart(TimestampMixins):
    CART_STATUS = [
        ('A', 'ACTIVE'),
        ('C', 'CONVERTED')
    ]
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=1, choices=CART_STATUS, default='A')
    grand_total = models.DecimalField(max_digits=8, decimal_places=2)
    checked_out_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"user-id:{self.user_id}---status:{'ACTIVE' if self.status=='A' else 'CONVERTED'}---cart-id:{self.id}"



class CartItem(TimestampMixins):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_variant_id = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    line_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"cart-id:{self.id}---product-variant:{self.product_variant_id}"