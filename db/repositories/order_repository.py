from db.connection import get_connection

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