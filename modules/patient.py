from db_config import DatabaseConnection
from exceptions.custom_expections import (
    DatabaseConnectionError,
    DuplicateRecordError,
    HMSBaseException,
)
from mysql.connector import Error, IntegrityError, ProgrammingError, InterfaceError

import re

from utils.custome_print import ColPt


class Patient:

    def add(self, patient_name, age, gender, phone_number, address):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        try:
            query = "INSERT INTO patients (patient_name, age, gender, phone_number, address) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (patient_name, age, gender, phone_number, address))
            conn.commit()
            new_id = cursor.lastrowid
            ColPt.green(f"[OK] Patient added sucessfully. ID = {new_id}")
        except InterfaceError as e:
            conn.rollback()
            ColPt.red(f"InterfaceError: {e.msg}")

        except IntegrityError as e:
            conn.rollback()
            key_name = re.search(r"key '[^.]+\.([^']+)'", e.msg).group(1)
            value_name = locals()[key_name]
            raise DuplicateRecordError("patients", key_name, value_name)

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
            cursor.execute("SELECT * FROM patients")
            return cursor.fetchall()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch patients data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)

    def get_by_id(self, id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM patients WHERE patient_id = %s"
            cursor.execute(query, (id,))
            return cursor.fetchone()
        except Error as e:
            raise DatabaseConnectionError(f"Failed to fetch patients data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)

    def update(self, patient_id, patient_name, age, gender, phone_number, address):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        try:
            fields, values = [], []
            if patient_name is not None and patient_name != "":
                fields.append("patient_name = %s")
                values.append(patient_name)

            if age is not None and age != "":
                fields.append("age = %s")
                values.append(age)

            if gender is not None and gender != "":
                fields.append("gender = %s")
                values.append(gender)

            if phone_number is not None and phone_number != "":
                fields.append("phone_number = %s")
                values.append(phone_number)

            if address is not None and address != "":
                fields.append("address = %s")
                values.append(address)

            values.append(patient_id)
            query = f"UPDATE patients SET {", ".join(fields)} WHERE patient_id = %s"
            cursor.execute(query, tuple(values))
            conn.commit()
            print(f"[OK] Patients {patient_id} has updated.")

        except Error as e:
            conn.rollback()
            raise DatabaseConnectionError(f"Failed to update Patient: {e}")
        finally:
            DatabaseConnection.close(conn, cursor)

    def delete(self, id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        try:
            query = "DELETE FROM patients WHERE patient_id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            print(f"[OK] Patient with {id} has deleted sucessfully.")
        except Error as e:
            conn.rollback()
            raise DatabaseConnectionError(f"Failed to delete Patient data: {e} ")
        finally:
            DatabaseConnection.close(conn, cursor)
