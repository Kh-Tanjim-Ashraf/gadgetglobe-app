from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart, CartItem
from product.models import ProductVariant
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages



def checkCart(request):
    return Cart.objects.get_or_create(
        user_id=request.user,
        status='A',
        defaults={
            'user_id': request.user,
        }
    )



@login_required
def cartDetail(request):
    # Check if the user has a cart with status 'ACTIVE', then show its cart-items, otherwise create a new cart
    cart, _ = checkCart(request)
    cartItems = CartItem.objects.filter(cart_id=cart).all()
    context = {
        'cart': cart,
        'cartItems': cartItems
    }
    return render(request, template_name='cart/detail.html', context=context)



def redirectOrigin(request):
    referer = request.META.get('HTTP_REFERER')
    is_safe = referer and url_has_allowed_host_and_scheme(
        url=referer,
        allowed_hosts={request.get_host()}, # Restricts to current domain
        require_https=request.is_secure()
    )
    if is_safe:
        return redirect(referer)
    return redirect('/')



@login_required
def addToCart(request, pk):
    if request.method == "POST":
        # Check the user has a cart with status 'ACTIVE', otherwise create a new cart
        cart, created = checkCart(request)

        # Check the product variant exists
        prod_v = get_object_or_404(ProductVariant, id=pk)
        
        # Check a valid purchase quantity is requested
        req_quantity = int(request.POST.get('quantity'))
        if req_quantity > prod_v.stock_unit:
            messages.success(request, message=f"Not enough stock!")
        
        else:
            line_total = prod_v.unit_price * req_quantity
            # Check same product variant exists in the same cart
            cart_item, created = CartItem.objects.get_or_create(
                cart_id=cart,
                product_variant_id=prod_v,
                defaults={
                    'cart_id': cart,
                    'product_variant_id': prod_v,
                    'quantity': req_quantity,
                    'unit_price': prod_v.unit_price,
                    'line_total': line_total
                }
            )

            # Update cart-item quantity
            if not created:
                cart_item.quantity += req_quantity
                # Recalculate the line_total w/ the unit_price, because if the unit price gets updated during this period, the customer will get inconsistent subtotal for stale unit price
                line_total = prod_v.unit_price * cart_item.quantity
                cart_item.line_total = line_total
                cart_item.save()

            messages.success(request, message=f"Added to cart!")
        
        # User stays in the same page
        return redirectOrigin(request)



@login_required
def deleteCartItem(request, pk):
    # Check cart item exists
    cart_item = get_object_or_404(CartItem, id=pk)
    cart_item.delete()
    return redirectOrigin(request)