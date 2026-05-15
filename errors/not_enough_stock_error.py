class NotEnoughStockError(Exception):
    def __init__(self, product_id):
        super().__init__(f"Not enough stock for product with id {product_id}")