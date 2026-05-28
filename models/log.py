class Log:
    def __init__(self, product_id, action_type, quantity_change, id = None, created_at = None, order_id = None, user_id = None):
        self.id = id
        self.product_id = product_id
        self.action_type = action_type
        self.created_at = created_at
        self.quantity_change = quantity_change
        self.order_id = order_id 
        self.user_id = user_id

    def __str__(self):
        return f'Product ID: {self.product_id} \n Action type: {self.action_type} \n Date: {self.created_at} \n Issued/Received: {self.quantity_change}'