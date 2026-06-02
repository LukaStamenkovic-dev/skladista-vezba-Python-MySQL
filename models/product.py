class Product:
    # ovde pitaj da li id svuda treba da bude = None kao u log.py ili je to jedinstveno, jer ti je AI reko da aplikacija 
    # treba da prati bazu a posto baza kreira te podatke treba da ih prosledimo kao None
    def __init__(self, name, price, is_active, id = None, created_at = None, updated_at = None):
        self.id = id
        self.name = name
        self.price = price
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        # i ovo mi nije najjasnije kako radi
        available = "Yes" if self.is_active else "No"
        return f'Product ID: {self.id} \n Name: {self.name} \n Available: {available} \n Price: {self.price}'