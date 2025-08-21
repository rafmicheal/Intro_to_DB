#!/usr/bin/python3
"""
A script that creates the database alx_book_store in MySQL server
"""

import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Connect to MySQL server (no database selected yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Asusmicheal6314@@##"   # put your MySQL root password here if set
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")  # optional


if __name__ == "__main__":
    create_database()
