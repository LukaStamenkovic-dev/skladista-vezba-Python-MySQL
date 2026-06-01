from db.repositories.product_repository import ProductRepository
from models.product import Product

def create_product(name, price):
    if price > 0 and name.strip():
        product = Product(name, price, is_active=True)
        product_repository = ProductRepository()
        product_repository.create_product(product)
        return product

def get_all_products():
    return ProductRepository().get_all_products()
