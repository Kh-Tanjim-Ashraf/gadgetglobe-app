from django.contrib import admin
from product.models import Brand, FeaturedBrand, Category, FeaturedCategory, Product, ProductAttribute, AttributeValue, ProductVariant, ProductImage



admin.site.register(Brand)
admin.site.register(FeaturedBrand)
admin.site.register(Category)
admin.site.register(FeaturedCategory)
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(AttributeValue)
admin.site.register(ProductVariant)
admin.site.register(ProductImage)