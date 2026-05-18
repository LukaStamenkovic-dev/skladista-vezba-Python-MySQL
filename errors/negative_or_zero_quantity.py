class QuantityValueError(Exception):
    def __init__(self, quantity):
        super().__init__(f"Invalid quantity: {quantity})")