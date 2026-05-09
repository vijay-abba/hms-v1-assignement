from db_config import DatabaseConnection
from exceptions.custom_expections import (
    DatabaseConnectionError,
    DuplicateRecordError,
    HMSBaseException,
)
from mysql.connector import Error, IntegrityError, ProgrammingError, InterfaceError
from rich.console import Console
import re

console = Console()


class Department:

    def add(self, department_name, department_code):

        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        try:

            query = """
                INSERT INTO departments (department_name, department_code)
                VALUES (%s,  %s)  
                """
            ex_res = cursor.execute(query, (department_name, department_code))
            conn_res = conn.commit()
            print("inserted")

            print(ex_res)
            print(conn_res)

            print(conn)
            print(cursor)
        except InterfaceError as e:
            conn.rollback()
            print(f"InterfaceError: {e.msg} ")
        except IntegrityError as e:
            # 1062 (23000): Duplicate entry 'department' for key 'departments.department_name'
            # key_name = list(map(lambda x: x.replace("'", "").strip(), e.msg.split("key")))[1].split(".")[1]
            # print("---")

            print(f"IntegrityError: {e} ")
            conn.rollback()
            key_name = re.search(r"key '[^.]+\.([^']+)'", e.msg).group(1)
            print(key_name)

            field_values = {
                "department_name": department_name,
                "department_code": department_code,
            }

            raise DuplicateRecordError("department", key_name, field_values[key_name])
        except ProgrammingError as e:
            console.print(f"ProgrammingError: Invalid SQL syntax {e}", style="bold red")
        except Error as e:
            console.print(e)
            conn.rollback()
            console.print(f"Something went Wrong {e}", style="bold red")
        finally:
            DatabaseConnection.close(conn, cursor)

    


try:
    d = Department()
    d.add("department", "dep")
except HMSBaseException as e:
    print(f"{e}")
