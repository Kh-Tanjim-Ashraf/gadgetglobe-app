from django.urls import path
from cart.views import cartDetail, addToCart, deleteCartItem


urlpatterns = [
    path('', view=cartDetail, name='cartDetail'),
    path('add-to-cart/<int:pk>/', view=addToCart, name='addToCart'),
    path('delete-cart-item/<int:pk>/', view=deleteCartItem, name='deleteCartItem')
]
