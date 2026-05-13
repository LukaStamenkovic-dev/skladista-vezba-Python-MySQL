# receive_product, issue_product (check quantity, lower_quantity, log) (if quantity > stock: raise Exception("Not enough stock"))
from db.repositories.inventory_repository import get_by_product_id
from db.repositories.inventory_repository import update_quantity

def issue_stock(product_id, quantity):
    inventory = get_by_product_id(product_id)
    if not inventory:
        raise Exception("Product not available")
    # ovde mora ovako jer jer moj repository trenutno vraća: cursor.fetchone() što vraća tuple, ne Inventory objekat.
    current_stock = inventory[2]
    if current_stock < quantity:
        raise Exception("Not enough stock")
    
    new_quantity = current_stock - quantity
    update_quantity(product_id, new_quantity)
