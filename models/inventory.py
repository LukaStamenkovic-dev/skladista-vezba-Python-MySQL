class Inventory:
    def __init__(self, id, product_id, quantity, minimum_threshold):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.minimum_threshold = minimum_threshold