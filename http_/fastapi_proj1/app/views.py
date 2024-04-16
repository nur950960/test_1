from typing import List
from fastapi import APIRouter, HTTPException

from .serializer import ProductCreateSerializer, ProductSerializer, ProductUpdateSerializer 
from .models import Product 
from settings import SessionLocal

db = SessionLocal()
router = APIRouter() 

@router.get('/products', response_model=List[ProductSerializer])
def product_list(): 
    products = db.query(Product).all()
    if not products:
        raise HTTPException(status_code=404, detail='Products not found') 
    return products 

@router.get('/products/{id}', response_model=ProductSerializer)
def product_details(id: int): 
    product = db.query(Product).get(id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product

@router.post('/products', status_code=201)
def create_product(data: ProductCreateSerializer): 
    new_product = Product(
                title = data.title,
                price = data.price, 
                description = data.description
                )
    db.add(new_product) 
    db.commit()

@router.delete('/products/{id}', status_code=204)
def delete_product(id: int): 
    product = db.query(Product).get(id) 
    if not product: 
        raise HTTPException(404, 'Product not found') 
    db.delete(product) 
    db.commit()

@router.patch('/products/{id}', status_code=201)
def update_product(id: int, data:ProductUpdateSerializer): 
    product = db.query(Product).get(id) 
    if not product: 
        raise HTTPException(404, 'Product not found') 
    if data.title: 
        product.title = data.title 
    if data.price: 
        product.price = data.price 
    if data.description: 
        product.description = data.description 
    db.commit()
