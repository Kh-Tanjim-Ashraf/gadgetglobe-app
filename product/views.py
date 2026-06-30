from django.shortcuts import render, get_object_or_404
from product.models import ProductVariant


def productList(request):
    # Fetch all product variants
    prodVariants = ProductVariant.objects.all()
    context = {'prodVariants': prodVariants}
    return render(request, template_name='product/list.html', context=context)



def productDetail(request, pk):
    # Fetch product-variant record
    prod_v = get_object_or_404(ProductVariant, pk=pk)
    # Fetch images of product-variant
    prod_v_images = prod_v.images.all().first()
    print("image:", prod_v_images.image.url)
    context = {
        'productVariant': prod_v, 
        'images': prod_v_images
    }
    return render(request, template_name='product/detail.html', context=context)
