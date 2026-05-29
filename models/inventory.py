class Inventory:
    def __init__(self, id, product_id, quantity, minimum_threshold, created_at = None, updated_at = None):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.minimum_threshold = minimum_threshold
        self.created_at = created_at
        self.updated_at = updated_at