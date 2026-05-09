from utils.custome_print import ColPt


def dashboard_menu():
    while True:
        ColPt.blue("\n----- Dashboard -----")
        print("1. Summary Numbers")
        print("2. Top Doctors by Revenue")
        print("3. Patients per department")
        print("4. Monthly Revenue Trend")
        print("5. Pending payments")
        print("6. Most common treatments")
        print("0. Back")

        dash_choice = ColPt.input_yellow("Enter your choice: ").strip()

        if dash_choice == "1":
            print("1. Summary Numbers")
        elif dash_choice == "2":
            print("2. Top Doctors by Revenue")
        elif dash_choice == "3":
            print("3. Patients per department")
        elif dash_choice == "4":
            print("4. Monthly Revenue Trend")
        elif dash_choice == "5":
            print("5. Pending payments")
        elif dash_choice == "6":
            print("6. Most common treatments")
        elif dash_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
