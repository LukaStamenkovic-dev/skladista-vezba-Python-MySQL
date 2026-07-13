import mysql.connector 

def get_connection():
    # nije mi samo jasno tacno ova sintaksa
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="warehouse_management"
    )
    return conn


def close_connection(conn):
    if conn: # i ovo
        conn.close()

# Test uspesan!
# if __name__ == "__main__":
   # conn = get_connection()
   # print("Connected successfully!")
   # conn.close()