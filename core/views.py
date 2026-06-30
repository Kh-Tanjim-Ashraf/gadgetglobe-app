from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Brand, Category, ProductVariant


def homePage(request):
    # Fetch the featured-brands
    featured_brands = Brand.objects.filter(is_featured=True).all()
    # Fetch the featured-categories
    featured_categories = Category.objects.filter(is_featured=True).all()
    # Fetch the featured-product-variants
    featured_product_variants = ProductVariant.objects.filter(is_featured=True).all()

    context = {
        "featured_brands": featured_brands,
        "featured_categories": featured_categories,
        "featured_product_variants": featured_product_variants,
    }
    return render(request, template_name='homepage.html', context=context)


@login_required
def secretPage(request):
    return render(request, template_name='secret.html')