from rich.console import Console
from InputHandling.department_menu import department_menu
from InputHandling.patient_menu import patient_menu
from InputHandling.doctor_menu import doctor_menu
from InputHandling.appointment_menu import appointment_menu
from InputHandling.treatment_menu import treatment_menu
from InputHandling.billing_menu import billing_menu
from InputHandling.dashboard_menu import dashboard_menu

console = Console()


def main_menu():
    while True:
        console.print("*" * 45, style="bold blue")
        console.print("      HOSPITAL MANAGEMENT SYSTEM (HMS)", style="bold blue")
        console.print("*" * 45, style="bold blue")
        print("1. Department Management")
        print("2. Patient Management")
        print("3. Doctor Management")
        print("4. Appointment Management")
        print("5. Treatment Management")
        print("6. Billing Management")
        print("7. Dashboard")
        print("0. Exit")
        user_choice = console.input("[bold yellow] Enter your choice: ").strip()
        # fmt: off
        if user_choice == "1": department_menu()
        elif user_choice == "2": patient_menu()
        elif user_choice == "3": doctor_menu()
        elif user_choice == "4": appointment_menu()
        elif user_choice == "5": treatment_menu()
        elif user_choice == "6": billing_menu()
        elif user_choice == "7": dashboard_menu()
        elif user_choice == "0":
            console.print("Thank you !", style="bold green")
            break
        else:
            console.print("Invalid Choice, Please Try Again!", style="bold red")
        # fmt: on


main_menu()
