
from utils.custome_print import ColPt


def treatment_menu():
    while True:
        ColPt.blue("\n----- Treatment Management -----")
        print("1. Add Treatment")
        print("2. View All Treatments")
        print("3. Get Treatment By ID")
        print("4. Update Treatment")
        print("5. Delete Treatment")
        print("6. View Treatments By Appointment")
        print("0. Back")

        treat_choice = ColPt.input_yellow("[bold yellow] Enter your choice: ").strip()

        if treat_choice == "1":
            print("1. Add Treatment")
        elif treat_choice == "2":
            print("2. View All Treatments")
        elif treat_choice == "3":
            print("3. Get Treatment By ID")
        elif treat_choice == "4":
            print("4. Update Treatment")
        elif treat_choice == "5":
            print("5. Delete Treatment")
        elif treat_choice == "6":
            print("6. View Treatments By Appointment")
        elif treat_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
