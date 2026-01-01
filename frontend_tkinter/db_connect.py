# db_connect.py
import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",        # Don’t change this unless MySQL is remote
            user="root",             # Your MySQL username
            password="",# Replace with your actual MySQL password
            database="certificate_db"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"❌ Database Connection Failed: {err}")
        return None
