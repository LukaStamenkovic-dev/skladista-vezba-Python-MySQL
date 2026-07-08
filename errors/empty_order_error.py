class EmptyOrderError(Exception):
    def __init__(self, quantity):
        super().__init__(f"Order must contain at least one product.")