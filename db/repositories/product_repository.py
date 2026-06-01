from db.connection import get_connection
from models.product import Product

class ProductRepository:

    def create_product(self, product):
        conn = get_connection()

        cursor = conn.cursor()

        query = "INSERT INTO products (name, price, is_active) VALUES (%s, %s, %s)"

        cursor.execute(query, (product.name, product.price, product.is_active))

        conn.commit()
        cursor.close()
        conn.close()

        #U pravim sistemima često vraćaš: created product, created id, affected rows, success object. Da li treba ovde tako?
        return True
    
    def get_all_products(self):
        conn = get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM products"

        cursor.execute(query)

        result = cursor.fetchall()
        rows_list = []
        for i in result:
            product = Product(
            id=i[0],
            name=i[1],
            price=i[2],
            is_active=i[3],
            created_at=i[4],
            updated_at=i[5]
    )
            rows_list.append(product)

        cursor.close()
        conn.close()

        return rows_list