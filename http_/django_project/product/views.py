# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404
# # from rest_framework.viewsets import ViewSet

# from .models import Category, Product
# from .serializers import ProductSerializers
# # # Create your views here.

# # class GetProductsView(APIView): 
# #     def get(self, request): 
# #         queryset = Product.objects.all() 
# #         serializer = ProductSerializers(data=queryset, many=True)
# #         serializer.is_valid()
# #         return Response(serializer.data)
    
# # class CreateProductView(APIView):
# #     # def post(self, request): 
# #     #     category_ = Category.objects.get(id=request.data['category'])
# #     #     product = Product.objects.create(
# #     #         title = request.data['title'],
# #     #         price = request.data['price'], 
# #     #         category = category_
# #     #     )
# #     #     return Response('HELLO')
    
# #     def post(self, request): 
# #         data = request.data 
# #         serializer = ProductSerializers(data=data) 
# #         if serializer.is_valid(): 
# #             serializer.save() 
# #             return Response(serializer.data)
# #         return Response(serializer.errors)
    
# # class GetProductView(APIView): 
# #     def get(self, request, pk): 
# #         queryset = Product.objects.get(id=pk) 
# #         serializer = ProductSerializers(data=queryset)
# #         if  serializer.is_valid():
# #             return Response(serializer.data)
# #         return Response(serializer.errors)


# @api_view(['GET'])
# def get_products(request): 
#     queryset = Product.objects.all()
#     serializer = ProductSerializers(queryset, many=True)
#     return Response(serializer.data, status=200) 

# @api_view(['POST'])
# def create_product(request):
#     serializer = ProductSerializers(data=request.data)
#     serializer.is_valid(raise_exception=True) 
#     serializer.save()
#     return Response(status=201)

# @api_view(['GET', 'DELETE'])
# def get_product(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'GET':
#         serializer = ProductSerializers(instance=product)
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         title_product = product.title
#         product.delete()
#         return Response(f'Успешно удален {title_product}')
    
# @api_view(['PATCH', 'PUT'])
# def update_product(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'PATCH': 
#         serializer = ProductSerializers(instance=product, data=request.data, partial=True) 
#         if serializer.is_valid(raise_exception=True): 
#             serializer.save()
#             return Response('Частичное изменинеею.')
#     elif request.method == 'PUT': 
#         serializer = ProductSerializers(instance=product, data=request.data) 
#         if serializer.is_valid(raise_exception=True): 
#             serializer.save()
#             return Response('Полное изменение.')

    




''' 
code 2 

'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import *

from .models import Product
from .serializers import ProductSerializers


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # permission_classes = [IsAuthenticatedOrReadOnly]
