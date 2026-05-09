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
            query = """
                INSERT INTO departments (department_name, department_code)
                VALUES (%s,  %s)  
                """
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


try:
    d = Department()
    d.add("department1", "dep1")
except HMSBaseException as e:
    print(f"{e}")
