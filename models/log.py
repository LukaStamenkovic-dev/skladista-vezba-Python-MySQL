class Log:
    def __init__(self, product_id, action_type, quantity_change, id = None, created_at = None, order_id = None, user_id = None):
        self.id = id
        self.product_id = product_id
        self.action_type = action_type
        self.created_at = created_at
        self.quantity_change = quantity_change
        self.order_id = order_id 
        self.user_id = user_id
