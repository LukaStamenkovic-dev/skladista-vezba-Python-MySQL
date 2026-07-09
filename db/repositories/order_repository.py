from db.connection import get_connection
from models.order import Order

class OrderRepository:

    def create_order(self, order):
        conn = get_connection()

        cursor = conn.cursor()

        query = "INSERT INTO orders (status, expected_delivery_date, total_price) VALUES (%s, %s, %s)"

        cursor.execute(query, (order.status, order.expected_delivery_date, order.total_price,))

        order_id = cursor.lastrowid
        
        conn.commit()
        cursor.close()
        conn.close()

        return order_id
    
    def get_order_by_id(self, order_id):
                
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM orders WHERE id = %s"

        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        
        if not result:
            order = None
        else:
            order = Order(
                id=result[0],
                status=result[1],
                created_at=result[2],
                expected_delivery_date=result[3],
                total_price=result[4])
            
        cursor.close()
        conn.close()

        return order