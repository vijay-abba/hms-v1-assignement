from db_config import DatabaseConnection
from exceptions.custom_expections import (
    DatabaseConnectionError,
    DuplicateRecordError,
    HMSBaseException,
)
from mysql.connector import Error, IntegrityError, ProgrammingError, InterfaceError

import re

from utils.custome_print import ColPt


class Department:

    def add(self, department_name, department_code):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        try:
            query = "INSERT INTO departments (department_name, department_code) VALUES (%s, %s)"
            cursor.execute(query, (department_name, department_code))
            conn.commit()
            new_id = cursor.lastrowid
            ColPt.green(f"[OK] Department added sucessfully. ID = {new_id}")
        except InterfaceError as e:
            conn.rollback()
            ColPt.red(f"InterfaceError: {e.msg}")

        except IntegrityError as e:
            conn.rollback()
            key_name = re.search(r"key '[^.]+\.([^']+)'", e.msg).group(1)
            value_name = locals()[key_name]
            raise DuplicateRecordError("department", key_name, value_name)

        except ProgrammingError as e:
            conn.rollback()
            ColPt.red(f"ProgrammingError: Invalid SQL syntax {e}")

        except Error as e:
            conn.rollback()
            ColPt.red(f"Something went Wrong {e}")

        finally:
            DatabaseConnection.close(conn, cursor)

    def get_all(self):

        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM departments")
            return cursor.fetchall()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch departements data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)

    def get_by_id(self, id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM departments WHERE department_id = %s"
            cursor.execute(query, (id,))
            return cursor.fetchone()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch departements data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)

    def update(self, department_id, department_name=None, department_code=None):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        try:
            fields, values = [], []
            if department_name is not None and department_name != "":
                fields.append("department_name = %s")
                values.append(department_name)

            if department_code is not None and department_code != "":
                fields.append("department_code = %s")
                values.append(department_code)

            values.append(department_id)
            query = (
                f"UPDATE departments SET {", ".join(fields)} WHERE department_id = %s"
            )
            cursor.execute(query, tuple(values))
            conn.commit()
            print(f"[OK] Department {department_id} has updated.")

        except Error as e:
            conn.rollback()
            raise DatabaseConnectionError(f"Failed to update department: {e}")
        finally:
            DatabaseConnection.close(conn, cursor)

    def delete(self, id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        try:
            query = "DELETE FROM departments WHERE department_id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            print(f"[OK] Department with {id} has deleted sucessfully.")
        except Error as e:
            conn.rollback()
            raise DatabaseConnectionError(f"Failed to delete departements data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)
