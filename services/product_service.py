from db.repositories.product_repository import ProductRepository
from models.product import Product
from errors.invalid_product_error import InvalidProductError
from errors.product_not_found_error import ProductNotFoundError

def create_product(name, price):
    if not name.strip():
        raise InvalidProductError("Product name cannot be empty.")

    if price <= 0:
        raise InvalidProductError("Product price must be greater than 0.")


    product = Product(name, price, is_active=True)
    product_repository = ProductRepository()
    product_repository.create_product(product)
    return product

def get_all_products():
    return ProductRepository().get_all_products()

def get_product_by_id(product_id):
    product = ProductRepository().get_product_by_id(product_id)
    if product is None:
        raise ProductNotFoundError(product_id)
    
    return product

def update_product(product_id, name, price):
    if not name.strip():
        raise InvalidProductError("Product name cannot be empty.")

    if price <= 0:
        raise InvalidProductError("Product price must be greater than 0.")
    
    product = get_product_by_id(product_id)
    product.name = name
    product.price = price
    ProductRepository().update_product(product)
    return product

# Napravio sam kod za uklanjane proizvoda odnosno menjanje statusa ali ne znam da li treba da ga pozivam iz main.py
def deactivate_product(product_id):
    product = get_product_by_id(product_id)
    product.is_active = False
   
    ProductRepository().deactivate_product(product_id)
    return product