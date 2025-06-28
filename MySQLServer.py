import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password'  # <-- Replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Try to create the database
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as e:
                print(f"Error creating database: {e}")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL server: {e}")

    finally:
        # Close cursor and connection safely
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
