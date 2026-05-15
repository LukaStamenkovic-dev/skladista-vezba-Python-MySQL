from db.connection import get_connection
from models.inventory import Inventory

class InventoryRepository:

    def get_by_product_id(self, product_id):
        conn = get_connection()

        cursor = conn.cursor()

        query = "SELECT * FROM inventory WHERE product_id = %s"

        cursor.execute(query, (product_id,))

        result = cursor.fetchone()

        cursor.close()
        conn.close()
        
        if not result:
            return None
        
        return Inventory( result[0], result[1], result[2], result[3])
       
            

    
    def update_quantity(self, product_id, new_quantity):
        conn = get_connection()

        cursor = conn.cursor()

        query = "UPDATE inventory SET quantity = %s WHERE product_id = %s"

        cursor.execute(query, (new_quantity, product_id))

        conn.commit()
        cursor.close()
        conn.close()


