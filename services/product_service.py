from db.repositories.product_repository import ProductRepository
from models.product import Product
from errors.invalid_product_error import InvalidProductError

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
    return ProductRepository().get_product_by_id(product_id)
