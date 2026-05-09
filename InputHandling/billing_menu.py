from utils.custome_print import ColPt


def billing_menu():
    while True:
        ColPt.blue("\n----- Billing Management -----")
        print("1. Add Bill (manual)")
        print("2. Auto-Generate Bill from Treatments")
        print("3. View All Bills")
        print("4. Get Bill by ID")
        print("5. Update Bill")
        print("6. Delete Bill")
        print("0. Back")

        bill_choice = ColPt.input_yellow("Enter your choice: ").strip()

        if bill_choice == "1":
            print("1. Add Bill (manual)")
        elif bill_choice == "2":
            print("2. Auto-Generate Bill from Treatments")
        elif bill_choice == "3":
            print("3. View All Bills")
        elif bill_choice == "4":
            print("4. Get Bill by ID")
        elif bill_choice == "5":
            print("5. Update Bill")
        elif bill_choice == "6":
            print("6. Delete Bill")
        elif bill_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
