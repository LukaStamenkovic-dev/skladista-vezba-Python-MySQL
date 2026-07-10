class Order:
    def __init__(self, status, expected_delivery_date, total_price, id = None, created_at = None):
        self.status = status
        self.expected_delivery_date = expected_delivery_date
        self.total_price = total_price
        self.id = id
        self.created_at = created_at


    def __str__(self):
        return f'Order ID: {self.id} \n Status: {self.status} \n Delivery: {self.expected_delivery_date} \n Total price: {self.total_price}'
    

