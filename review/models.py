from django.db import models
from shared.models import TimestampMixins
from django.contrib.auth.models import User
from product.models import ProductVariant
from django.core.validators import MinValueValidator, MaxValueValidator



class Review(TimestampMixins):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product_variant_id = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    message = models.TextField(null=True, blank=True, help_text="Provide a product review.")

    def __str__(self):
        return f"Product: {self.product_variant_id.product_id.name[:20]}---Rating: {self.rating}---Message: {self.message[:10]}...."



class ReviewImage(TimestampMixins):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="review/")

    def __str__(self):
        return f"Review Image of product: {self.review_id.product_variant_id.product_id.name}"