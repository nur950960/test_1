# from django.urls import path 

# # from .views import GetProductsView, CreateProductView, GetProductView
# from .views import get_products, create_product, get_product, update_product

# urlpatterns = [
#     # path('get_products/', GetProductsView.as_view()),
#     # path('create_product/', CreateProductView.as_view()), 
#     # path('get_product/<int:pk>/', GetProductView.as_view()),
#     path('get_products/', get_products),
#     path('create_product/', create_product),
#     path('get_product/<int:id>/', get_product),
#     path('update_product/<int:id>/', update_product),
# ]





''' 
code 2

'''
from django.urls import path, include

from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]