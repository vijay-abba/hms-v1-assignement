from utils.custome_print import ColPt


def appointment_menu():
    while True:
        ColPt.blue("\n----- Appointment Management -----")
        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. Get Appointment By ID")
        print("4. Update Appointment")
        print("5. Delete Appointment")
        print("6. Cancel Appointment")
        print("0. Back")

        app_choice = ColPt.input_yellow("Enter your choice: ").strip()

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
            ColPt.red("Invalid Choice, Please Try Again!")
