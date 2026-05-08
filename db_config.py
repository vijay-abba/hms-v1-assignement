import mysql.connector
from mysql.connector import Error
from exceptions.custom_expections import DatabaseConnectionError
from rich.console import Console

console = Console()


# fmt: off
DB_CONFIG = {
    "host": "localhost", 
    "user": "root", 
    "database": "hms_db",
    "password": "root_password",
    "port": 3306,
    }
# fmt: on


class DatabaseConnection:

    @staticmethod
    def get_connection():

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            if conn.is_connected():
                console.print("Connected to Database sucessfully", style="bold green")
                return conn
            raise DatabaseConnectionError(
                "Connection Object is created but not connected"
            )
        except Error as e:
            raise DatabaseConnectionError(f"MySQL error: {e}")

    @staticmethod
    def close(conn, cursor=None):

        if cursor:
            cursor.close()
            print("connection closed for cursor")
        if conn and conn.is_connected():
            conn.close()
            print("connection closed for conn")

            
