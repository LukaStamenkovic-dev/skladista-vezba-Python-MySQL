from models.supplier import Supplier
from db.repositories.supplier_repository import SupplierRepository
from errors.invalid_supplier_error import InvalidSupplierError
from errors.supplier_not_found_error import SupplierNotFoundError




def create_supplier(name, location):
    if not name.strip():
        raise InvalidSupplierError("Supplier name cannot be empty.")

    if not location.strip():
        raise InvalidSupplierError("Location name cannot be empty.")


    supplier = Supplier(name, location)
    supplier_repository = SupplierRepository()
    supplier_repository.create_supplier(supplier)
    return supplier

def get_all_suppliers():
    return SupplierRepository().get_all_suppliers()

def get_supplier_by_id(supplier_id):
    supplier = SupplierRepository().get_supplier_by_id(supplier_id)

    if supplier is None:
        raise SupplierNotFoundError(supplier_id)
    
    return supplier

def update_supplier(supplier_id, name, location):
    if not name.strip():
        raise InvalidSupplierError("Supplier name cannot be empty.")

    if not location.strip():
        raise InvalidSupplierError("Location name cannot be empty.")

    
    supplier = get_supplier_by_id(supplier_id)
    supplier.name = name
    supplier.location = location
    SupplierRepository().update_supplier(supplier)
    return supplier