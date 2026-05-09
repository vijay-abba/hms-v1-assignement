import mysql.connector
from mysql.connector import Error
from exceptions.custom_expections import DatabaseConnectionError

from utils.custome_print import ColPt

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
                ColPt.green("Connected to Database sucessfully")
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
            ColPt.orange("connection closed for cursor")
        if conn and conn.is_connected():
            conn.close()
            ColPt.orange("connection closed for conn")

    @staticmethod
    def add():
        pass
