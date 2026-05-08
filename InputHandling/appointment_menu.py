from rich.console import Console

console = Console()


def appointment_menu():
    while True:
        console.print("\n----- Appointment Management -----", style="bold blue")
        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. Get Appointment By ID")
        print("4. Update Appointment")
        print("5. Delete Appointment")
        print("6. Cancel Appointment")
        print("0. Back")

        app_choice = console.input("[bold yellow] Enter your choice: ").strip()

        if app_choice == "1":
            print("1. Book Appointment")
        elif app_choice == "2":
            print("2. View All Appointments")
        elif app_choice == "3":
            print("3. Get Appointment By ID")
        elif app_choice == "4":
            print("4. Update Appointment")
        elif app_choice == "5":
            print("5. Delete Appointment")
        elif app_choice == "6":
           print("6. Cancel Appointment")
        elif app_choice == "0":
            break
        else:
            console.print("Invalid Choice, Please Try Again!", style="bold red")
