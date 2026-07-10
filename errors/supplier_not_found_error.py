class SupplierNotFoundError(Exception):
    def __init__(self, supplier_id):
        super().__init__(f"Supplier with id {supplier_id} not found")