from utils.custome_print import ColPt


def doctor_menu():
    while True:
        ColPt.blue("\n----- Doctor Management -----")
        print("1. Add Doctor")
        print("2. View All Doctor")
        print("3. Get Doctor By ID")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("0. Back")

        doc_choice = ColPt.input_yellow("Enter your choice: ").strip()

        if doc_choice == "1":
            print("1. Add Doctor")
        elif doc_choice == "2":
            print("2. View All Doctor")
        elif doc_choice == "3":
            print("3. Get Doctor By ID")
        elif doc_choice == "4":
            print("4. Update Doctor")
        elif doc_choice == "5":
            print("5. Delete Doctor")
        elif doc_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
