class Supplier:
    def __init__(self, name, location, id = None, created_at = None, updated_at = None):
        self.id = id
        self.name = name
        self.location = location
        self.created_at = created_at
        self.updated_at = updated_at

    # def __str__(self):
    #     # i ovo mi nije najjasnije kako radi u smislu kad se poziva
    #     available = "Yes" if self.is_active else "No"
    #     return f'Product ID: {self.id} \n Name: {self.name} \n Available: {available} \n Price: {self.price}'