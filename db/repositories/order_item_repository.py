from db.connection import get_connection

class OrderItemRepository:
    def create_order_item(order_item):
        conn = get_connection()

        cursor = conn.cursor()

        query = "INSERT INTO order_items (order_id, product_id, quantity, price_per_product) VALUES (%s, %s, %s, %s)"

        cursor.execute(query, (order_item.order_id, order_item.product_id, order_item.quantity, order_item.price_per_product,))

        
        conn.commit()
        cursor.close()
        conn.close()

        return True