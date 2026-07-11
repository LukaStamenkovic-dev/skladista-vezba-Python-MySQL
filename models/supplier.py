class Supplier:
    def __init__(self, name, location, id = None, created_at = None, updated_at = None):
        self.id = id
        self.name = name
        self.location = location
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f'Supplier ID: {self.id} \n Name: {self.name} \n Location: {self.location} \n'