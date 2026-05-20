from db.connection import get_connection
from models.log import Log

class LogRepository:
    
    def create_log(self, log):

        conn = get_connection()

        cursor = conn.cursor()

        query = "INSERT INTO logs (product_id, action_type, quantity_change) VALUES (%s, %s, %s)"

        cursor.execute(query, (log.product_id, log.action_type, log.quantity_change))

        conn.commit()
        cursor.close()
        conn.close()
        # zelim da vrati created log ID ali jos uvek nisam siguran kako to da izvedem
        return True

    def get_logs_by_product_id(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM logs WHERE product_id = %s"

        cursor.execute(query, (product_id,))

        result = cursor.fetchall()
        rows_list = []
        for i in result:
            log = Log(
            product_id=i[1],
            action_type=i[2],
            quantity_change=i[4],
            id=i[0],
            created_at=i[3],
            order_id=i[5],
            user_id=i[6]
    )
            rows_list.append(log)

        cursor.close()
        conn.close()
        

        
        
