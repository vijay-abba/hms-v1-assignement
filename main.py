from InputHandling.department_menu import department_menu
from InputHandling.patient_menu import patient_menu
from InputHandling.doctor_menu import doctor_menu
from InputHandling.appointment_menu import appointment_menu
from InputHandling.treatment_menu import treatment_menu
from InputHandling.billing_menu import billing_menu
from InputHandling.dashboard_menu import dashboard_menu

from utils.custome_print import ColPt
from input_handling import (
    InputHandling,
    InputHandlingBill,
    InputHandlingAppt,
    InputHandlingTreatment,
)


def print_options():
    ColPt.blue("*" * 45)
    ColPt.blue("      HOSPITAL MANAGEMENT SYSTEM (HMS)")
    ColPt.blue("*" * 45)
    print("1. Department Management")
    print("2. Patient Management")
    print("3. Doctor Management")
    print("4. Appointment Management")
    print("5. Treatment Management")
    print("6. Billing Management")
    print("7. Dashboard")
    print("0. Exit")


department_fields = {
    "department_id": "Department Id",
    "department_name": "Department Name",
    "department_code": "Department Code",
}
department = InputHandling(
    "Department", "departments", "department_id", department_fields
)

patient_fields = {
    "patient_id": "Patient Id",
    "patient_name": "Patient Name",
    "age": "Age",
    "gender": "Gender",
    "phone_number": "Phone Number",
    "address": "Address",
}
patient = InputHandling("Patient", "patients", "patient_id", patient_fields)


doctor_fields = {
    "doctor_id": "Doctor Id",
    "doctor_name": "Doctor  Name",
    "department_id": "Department Id",
    "speciality": "Speciality",
    "experience": "Experience",
}
doctor = InputHandling("Doctor", "doctors", "doctor_id", doctor_fields)

appointment_fields = {
    "appointment_id": "Appointment Id",
    "patient_id": "Patient Id",
    "doctor_id": "Doctor Id",
    "appointment_time": "Appointment Time",
    "appointment_status": "Appointment Status",
}

appointment = InputHandlingAppt(
    "Appointment", "appointments", "appointment_id", appointment_fields
)

treatment_fields = {
    "treatment_id": "treatment_id",
    "treatment_type": "treatment_type",
    "appointment_id": "appointment_id",
    "cost": "cost",
}

treatment = InputHandlingTreatment(
    "Treatment", "treatment", "treatment_id", treatment_fields
)


billing_fields = {
    "billing_id": "billing_id",
    "appointment_id": "appointment_id",
    "total_amount": "total_amount",
    "payment_status": "payment_status",
    "payment_type": "payment_type",
}

bill = InputHandlingBill("Bill", "billing", "billing_id", billing_fields)


def main_menu():
    while True:
        print_options()
        user_choice = ColPt.input_yellow("Enter your choice: ").strip()
        # fmt: off
        if user_choice == "1": department.run_process()
        elif user_choice == "2": patient.run_process()
        elif user_choice == "3": doctor.run_process()
        elif user_choice == "4": appointment.run_process()
        elif user_choice == "5": treatment.run_process()
        elif user_choice == "6": bill.run_process()
        elif user_choice == "7": dashboard_menu()
        elif user_choice == "0":
            ColPt.green("Thank you !")
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
        # fmt: on


try:
    main_menu()
except KeyboardInterrupt as e:
    ColPt.yellow(f"[Info] Operation cancelled by user")
except Exception as e:
    ColPt.red(f"[UNEXPECTED ERROR ] {e}")
