from db.repositories.order_repository import OrderRepository
from db.repositories.order_item_repository import OrderItemRepository
from models.order import Order
from datetime import date, timedelta

def create_order(items):
    today = date.today()
    delivery_time = timedelta(days=7)
    expected_delivery_date = today + delivery_time

    total_price = 0
    for item in items:
        total_price += item.quantity * item.price_per_product
    
    order = Order("PENDING", expected_delivery_date, total_price)

    order_id = OrderRepository().create_order(order)

    for item in items:
        item.order_id = order_id
        OrderItemRepository().create_order_item(item)

    return order