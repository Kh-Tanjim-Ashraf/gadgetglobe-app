from django.db import models
from shared.models import TimestampMixins, NamedSlugMixins
from shared.utils import random_alphanumeric


# Note: I'm only make the `name` attributes unique, since the `slug` attributes will be automatically generated, thus it's not required to make the `slug` attribute unique as well

class Brand(TimestampMixins, NamedSlugMixins):
    logo = models.ImageField(null=True, blank=True, upload_to="product/brand-logo/")
    website = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=50, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_brand_name"
            )
        ]
    
    def __str__(self):
        return self.name



class Category(TimestampMixins, NamedSlugMixins):
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)      # Category/Sub-category

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_category_name'
            )
        ]
    
    def __str__(self):
        return f"Category: {self.parent_id.name if self.parent_id else None}---Sub-category: {self.name}"



class Product(TimestampMixins, NamedSlugMixins):
    categories = models.ManyToManyField(Category, related_name='products')
    series = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100)
    brand_id = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)   # Regardless of brand-records, product-records should persist

    def __str__(self):
        return f"Brand: {self.brand_id}---Product: {self.name}"



# Product-Variant-Attribute (PAV) design model
class ProductAttribute(TimestampMixins):
    # TODO: Provide a searching feature in the "parent-id" input when an admin selects a parent-attribute for the sub-attribute.
    # TODO: Show only the parent attributes in the "parent-id" input
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)     # Attribute/Sub-attribute
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["parent_id", "name"],
                name="unique_parent_sub_attribute",
                # Not working as expected; TODO: Debug unique-together-fields (parent_id, name)
                violation_error_message="Sub-attributes should be unique in each parent-attribute"
            )
        ]

    def __str__(self):
        if not self.parent_id:
            return f"Parent-attribute: {self.name}"
        return f"Parent-attribute: {self.parent_id.name}---Sub-attribute: {self.name}"
        



class AttributeValue(TimestampMixins):
    product_attribute_id = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.TextField(help_text="Provide the values of each product attribute.")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product_attribute_id", "value"],
                name="unique_product_attribute_id_value"
            )
        ]

    def __str__(self):
        return f"{self.product_attribute_id.name}: {self.value}"



class ProductVariant(TimestampMixins):
    PRODUCT_VARIANT_STATUS = [
        ('IS', 'IN STOCK'),
        ('OOS', 'OUT OF STOCK'),
        ('PO', 'PRE ORDER'),
        ('CFP', 'CALL FOR PRICE'),
    ]
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=PRODUCT_VARIANT_STATUS, default='IS')
    manufacturer_part_number = models.CharField(max_length=100, null=True, blank=True)
    sku = models.CharField(max_length=24, null=True, blank=True)
    stock_unit = models.PositiveIntegerField(default=0)
    attribute_values = models.ManyToManyField(AttributeValue, related_name='product_variants')
    # TODO: Define the `description` as markdown field including a markdown-editor in the admin-panel
    description = models.TextField(null=True, blank=True, help_text="Provide a concise description of the product variant.")
    stripe_product_variant_id = models.CharField(max_length=30, null=True, blank=True)
    stripe_price_id = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"Brand: {self.product_id.brand_id}---Product: {self.product_id.name}---Model: {self.manufacturer_part_number}"
    
    def save(self, *args, **kwargs):
        # Total SKU length=24 (Include hyphens in-between)
        if not self.sku:
            self.sku = f"{self.product_id.brand_id.name[:5]}-{self.product_id.model[:5]}-{self.manufacturer_part_number[:5] if self.manufacturer_part_number else random_alphanumeric()}-{random_alphanumeric()}"
        return super().save(*args, **kwargs)



class ProductImage(TimestampMixins):
    product_variant_id = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/product-image/")

    def __str__(self):
        return f"Image of {self.product_variant_id.product_id.name}"