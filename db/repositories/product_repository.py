from db.connection import get_connection
from models.product import Product

class ProductRepository:

    def create_product(self, product):
        conn = get_connection()

        cursor = conn.cursor()

        query = "INSERT INTO products (name, price, is_active) VALUES (%s, %s, %s, %s)"

        cursor.execute(query, (product.name, product.price, product.is_active))

        conn.commit()
        cursor.close()
        conn.close()

        #U pravim sistemima često vraćaš: created product, created id, affected rows, success object. Da li treba ovde tako?
        return True