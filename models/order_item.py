class OrderItem:
    def __init__(self, product_id, quantity, price_per_product, order_id=None, id=None):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price_per_product = price_per_product
        self.id = id




