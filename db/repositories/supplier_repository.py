from db.connection import get_connection
from models.supplier import Supplier

class SupplierRepository:

    def create_supplier(self, supplier):
        conn = get_connection()

        cursor = conn.cursor()

        query = "INSERT INTO suppliers (name, location) VALUES (%s, %s)"

        cursor.execute(query, (supplier.name, supplier.location))

        conn.commit()
        cursor.close()
        conn.close()

        return True
    
    def get_all_suppliers(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM suppliers"

        cursor.execute(query)

        result = cursor.fetchall()
        rows_list = []
        for i in result:
            supplier = Supplier(
            id=i[0],
            name=i[1],
            location=i[2],
            created_at=i[3],
            updated_at=i[4]
    )
            rows_list.append(supplier)

        cursor.close()
        conn.close()

        return rows_list
    
    def get_supplier_by_id(self, supplier_id):
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM suppliers WHERE id = %s"

        cursor.execute(query, (supplier_id,))
        result = cursor.fetchone()
        
        if not result:
            supplier = None
        else:
            supplier = Supplier(
            id=result[0],
            name=result[1],
            location=result[2],
            created_at=result[3],
            updated_at=result[4])
            
        cursor.close()
        conn.close()

        return supplier
    
    def update_supplier(self, supplier):
        conn = get_connection()
        cursor = conn.cursor()

        query = "UPDATE suppliers SET name = %s, location = %s WHERE id = %s"

        cursor.execute(query, (supplier.name, supplier.location, supplier.id))

        conn.commit()
        cursor.close()
        conn.close()

        return supplier