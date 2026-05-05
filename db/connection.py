import mysql.connector 

def get_connection():
    # nije mi samo jasno tacno ova sintaksa
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_database"
    )
    return conn


def close_connection(conn):
    if conn:
        conn.close()