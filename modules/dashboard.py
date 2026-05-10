from db_config import DatabaseConnection
from exceptions.custom_expections import (
    DatabaseConnectionError,
    DuplicateRecordError,
    HMSBaseException,
)
from mysql.connector import Error, IntegrityError, ProgrammingError, InterfaceError

import re

from utils.custome_print import ColPt

query_obj = {
    # summary_query
    "1": """
            SELECT 
                (SELECT COUNT(*) FROM patients) AS total_patients,
                (SELECT COUNT(*) FROM doctors) AS total_doctors,
                (SELECT COUNT(*) FROM departments) AS total_departments,
                (SELECT COUNT(*) FROM appointments) AS total_appointments,
                
                COALESCE((SELECT SUM(total_amount) FROM billing WHERE payment_status = 'Paid'), 0) AS paid_revenue,
                COALESCE((SELECT SUM(total_amount) FROM billing WHERE payment_status = 'Pending'), 0) AS pending_revenue,
                COALESCE((SELECT SUM(total_amount) FROM billing WHERE payment_status = 'Cancelled'), 0) AS cancelled_revenue;

            """,
    # top_doctors_query
    "2": """
            SELECT 
                d.doctor_id,
                d.doctor_name,
                d.speciality,
                SUM(b.total_amount) AS total_revenue
            FROM 
                doctors d
            JOIN 
                appointments a ON d.doctor_id = a.doctor_id
            JOIN 
                billing b ON a.appointment_id = b.appointment_id
            WHERE 
                b.payment_status = 'Paid'
            GROUP BY 
                d.doctor_id, 
                d.doctor_name, 
                d.speciality
            ORDER BY 
                total_revenue DESC
            LIMIT 5;
            """,
    # patients_per_departmanet
    "3": """
            SELECT 
                d.department_name,
                COUNT(DISTINCT a.patient_id) AS unique_patients,
                COUNT(a.appointment_id) AS total_appointments
            FROM 
                departments d
            LEFT JOIN 
                doctors doc ON d.department_id = doc.department_id
            LEFT JOIN 
                appointments a ON doc.doctor_id = a.doctor_id
            GROUP BY 
                d.department_id, 
                d.department_name
            ORDER BY 
                total_appointments DESC;
            """,
    # monthly_revenue
    "4": """
            SELECT 
                DATE_FORMAT(a.appointment_time, '%Y-%m') AS revenue_month,
                SUM(b.total_amount) AS monthly_revenue
            FROM 
                billing b
            JOIN 
                appointments a ON b.appointment_id = a.appointment_id
            WHERE 
                b.payment_status = 'Paid'
                -- Filters for records within the last 12 months from today
                AND a.appointment_time >= DATE_SUB(CURRENT_DATE, INTERVAL 12 MONTH)
            GROUP BY 
                DATE_FORMAT(a.appointment_time, '%Y-%m')
            ORDER BY 
                revenue_month ASC;
            """,
    # pending_payments
    "5": """
            SELECT 
                p.patient_name,
                p.phone_number,
                b.total_amount AS pending_amount,
                a.appointment_time
            FROM 
                billing b
            JOIN 
                appointments a ON b.appointment_id = a.appointment_id
            JOIN 
                patients p ON a.patient_id = p.patient_id
            WHERE 
                b.payment_status = 'Pending'
            ORDER BY 
                a.appointment_time ASC;
            """,
    # most_common_treatments
    "6": """
            SELECT 
                treatment_type,
                COUNT(treatment_id) AS treatment_count,
                ROUND(AVG(cost), 2) AS average_cost,
                SUM(cost) AS total_cost
            FROM 
                treatment
            GROUP BY 
                treatment_type
            ORDER BY 
                treatment_count DESC, 
                total_cost DESC;
            """,
    # age_group
    "7": """
                SELECT 
                    CASE 
                        WHEN age BETWEEN 0 AND 18 THEN '0-18 Years'
                        WHEN age BETWEEN 19 AND 35 THEN '19-35 Years'
                        WHEN age BETWEEN 36 AND 50 THEN '36-50 Years'
                        WHEN age BETWEEN 51 AND 65 THEN '51-65 Years'
                        ELSE '66+ Years' 
                    END AS age_group,
                    COUNT(*) AS patient_count
                FROM 
                    patients
                GROUP BY 
                    age_group
                ORDER BY 
                    -- This clever trick ensures the groups sort chronologically 
                    -- rather than alphabetically by the group name text
                    MIN(age) ASC;
                """,
    # doctor_utilization
    "8": """
            SELECT 
                d.doctor_name,
                COUNT(a.appointment_id) AS total_appointments,
                SUM(CASE WHEN a.appointment_status = 'Completed' THEN 1 ELSE 0 END) AS completed_appointments,
                SUM(CASE WHEN a.appointment_status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_appointments,
                
                -- Calculates the percentage of completed appointments out of the total
                -- NULLIF prevents a "divide by zero" error if a doctor has 0 appointments
                ROUND((SUM(CASE WHEN a.appointment_status = 'Completed' THEN 1 ELSE 0 END) / 
                    NULLIF(COUNT(a.appointment_id), 0)) * 100, 2) AS completion_rate_percent
            FROM 
                doctors d
            LEFT JOIN 
                appointments a ON d.doctor_id = a.doctor_id
            GROUP BY 
                d.doctor_id, 
                d.doctor_name
            ORDER BY 
                completion_rate_percent DESC, 
                total_appointments DESC;
            """,
}


class Dashboard:

    @staticmethod
    def summary(choice):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            query = query_obj[choice]
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            conn.rollback()
            ColPt.red(f"Something went Wrong {e}")
        finally:
            DatabaseConnection.close(conn, cursor)

        # fmt: off
