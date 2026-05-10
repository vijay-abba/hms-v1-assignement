from db_config import DatabaseConnection
from exceptions.custom_expections import (
    DatabaseConnectionError,
    DuplicateRecordError,
    HMSBaseException,
)
from mysql.connector import Error, IntegrityError, ProgrammingError, InterfaceError

import re

from utils.custome_print import ColPt


class DatabaseAction:

    @staticmethod
    def add(table_name, payload):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        try:
            fields, values, placeholders = [], [], []

            for key, value in payload.items():
                fields.append(key)
                values.append(value)
                placeholders.append("%s")

            query = f"INSERT INTO {table_name} ({", ".join(fields)}) VALUES ({", ".join(placeholders)})"
            cursor.execute(query, tuple(values))
            conn.commit()
            new_id = cursor.lastrowid
            ColPt.green(f"[OK] {table_name} added sucessfully. ID = {new_id}")
        except InterfaceError as e:
            conn.rollback()
            ColPt.red(f"InterfaceError: {e.msg}")
        except IntegrityError as e:
            conn.rollback()
            key_name = re.search(r"key '[^.]+\.([^']+)'", e.msg).group(1)
            value_name = locals()["payload"][key_name]
            raise DuplicateRecordError(table_name, key_name, value_name)
        except ProgrammingError as e:
            conn.rollback()
            ColPt.red(f"ProgrammingError: Invalid SQL syntax {e}")
        except Error as e:
            conn.rollback()
            ColPt.red(f"Something went Wrong {e}")
        finally:
            DatabaseConnection.close(conn, cursor)


    @staticmethod
    def get_all(table_name):

        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            return cursor.fetchall()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch {table_name} data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)

    @staticmethod
    def get_by_id(table_name, id_name, id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            query = f"SELECT * FROM {table_name} WHERE {id_name} = %s"
            cursor.execute(query, (id,))
            return cursor.fetchone()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch {table_name} data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)

    @staticmethod
    def update(table_name, id_name, payload):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        try:
            id = payload.get(id_name)
            fields, values = [], []
            for key, val in payload.items():
                if val is not None and val != "":
                    fields.append(f"{key} = %s")
                    values.append(val)

            values.append(id)
            query = f"UPDATE {table_name} SET {", ".join(fields)} WHERE {id_name} = %s"
            cursor.execute(query, tuple(values))
            conn.commit()
            print(f"[OK] {table_name} {id} has updated.")
        except Error as e:
            conn.rollback()
            raise DatabaseConnectionError(f"Failed to update department: {e}")
        finally:
            DatabaseConnection.close(conn, cursor)
        return

    @staticmethod
    def delete(table_name, id_name, id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        try:
            query = f"DELETE FROM {table_name} WHERE {id_name} = %s"
            cursor.execute(query, (id,))
            conn.commit()
            print(f"[OK] {table_name} with {id} has deleted sucessfully.")
        except Error as e:
            conn.rollback()
            raise DatabaseConnectionError(f"Failed to delete {table_name} data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)

"""
print("__sf")
from InputHandling.safe_run import safe_run

# safe_run(d.add, "departments", {"department_name": "Psychiatry", "department_code": "PSY"})


patient_data = {
    "patient_name": "Pushpa",
    "age": "32",
    "gender": "Male",
    "phone_number": "s99999",
    "address": "HYD",
}

# safe_run(DatabaseAction.add, "patients", patient_data)
# safe_run(DatabaseAction.get_all, "patients")

# safe_run(DatabaseAction.get_by_id, "patients", {"patient_id": "0"})
# safe_run(DatabaseAction.get_by_id, "departments", {"department_id": "797"})

# department_id, department_name=None, department_code=None

patient_data = {
    "patient_id": "6",
    "patient_name": "Pushpa Raj",
    "age": "40",
    "gender": "Male",
    "phone_number": "s99999X100",
    "address": "CHITOOR",
}
# safe_run(DatabaseAction.update("patients", "patient_id", patient_data))

dep_data = {
    "department_id": "65",
    "department_name": "Physiotherapy-DP",
    "department_code": "PHY-DP",
}

# safe_run(DatabaseAction.update("departments", "department_id", dep_data))


safe_run(DatabaseAction.get_by_id, "patients", "patient_id", "1")
safe_run(DatabaseAction.get_by_id, "departments", "department_id", "74")

"""