# receive_product, issue_product (check quantity, lower_quantity, log) (if quantity > stock: raise Exception("Not enough stock"))
from db.repositories.inventory_repository import InventoryRepository
from errors.product_not_found_error import ProductNotFoundError
from errors.not_enough_stock_error import NotEnoughStockError
from errors.negative_or_zero_quantity import QuantityValueError

def issue_stock(product_id, quantity):
    if quantity <= 0:
        raise QuantityValueError(quantity)
    
    inventory_repository = InventoryRepository()
    inventory = inventory_repository.get_by_product_id(product_id)
    if inventory is None:
        raise ProductNotFoundError(product_id)

    current_stock = inventory.quantity
    if current_stock < quantity:
        raise NotEnoughStockError(product_id)
    
    new_quantity = current_stock - quantity
    inventory_repository.update_quantity(product_id, new_quantity)


def receive_stock(product_id, quantity): 
    if quantity <= 0:
        raise QuantityValueError(quantity)
    
    inventory_repository = InventoryRepository()
    inventory = inventory_repository.get_by_product_id(product_id)
    if inventory is None:
        raise ProductNotFoundError(product_id)
    current_stock = inventory.quantity
    new_quantity = current_stock + quantity
    inventory_repository.update_quantity(product_id, new_quantity)




