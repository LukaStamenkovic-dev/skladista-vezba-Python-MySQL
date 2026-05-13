from db.connection import get_connection

def get_by_product_id(product_id):
    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM inventory WHERE product_id = %s"

    cursor.execute(query, (product_id,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

    
def update_quantity(product_id, new_quantity):
    conn = get_connection()

    cursor = conn.cursor()

    query = "UPDATE inventory SET quantity = %s WHERE product_id = %s"

    cursor.execute(query, (new_quantity, product_id))

    conn.commit()
    cursor.close()
    conn.close()


