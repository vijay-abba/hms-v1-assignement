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
            keys, values, placeholders = [], [], []

            for key, value in payload.items():
                keys.append(key)
                values.append(value)
                placeholders.append("%s")

            query = f"INSERT INTO {table_name} ({", ".join(keys)}) VALUES ({", ".join(placeholders)})"
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
            print("---")

    @staticmethod
    def get_all(table_name):

        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            print(rows)
            return rows
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch departements data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)


print("---")
# d = DatabaseAction()


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
safe_run(DatabaseAction.get_all, "patients")
safe_run(DatabaseAction.get_all, "departments")

