from django.urls import path
from product.views import productList, productDetail


urlpatterns = [
    path('', view=productList, name='productList'),
    path('<int:pk>/', view=productDetail, name='productDetail'),
]