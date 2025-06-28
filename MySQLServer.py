import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password'  # <-- Change this to your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Try to create database
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error creating database: {e}")

    except Error as e:
        print(f"Error while connecting to MySQL server: {e}")

    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")  # Optional: Uncomment if you want

if __name__ == "__main__":
    create_database()
