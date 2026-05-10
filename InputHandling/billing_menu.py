from utils.custome_print import ColPt
from InputHandling.safe_run import safe_run
from tabulate import tabulate
from db_action import DatabaseAction


def billing_menu():

    # TASK: PENDING DOC
    DISPLY_NAME = "Bill"
    table_name = "Bill"
    pri_id_name = "billing_id"

    while True:
        ColPt.blue(f"\n----- {DISPLY_NAME} Management -----")
        print(f"1. Add {DISPLY_NAME}")
        print("2. Auto-Generate Bill from Treatments")
        print(f"3. View All {DISPLY_NAME}s")
        print(f"4. Get {DISPLY_NAME} By ID")
        print(f"5. Update {DISPLY_NAME}")
        print(f"6. Delete {DISPLY_NAME}")
        print(f"0. Back")

        choice = ColPt.input_yellow("Enter your choice: ").strip()

        if choice == "1":
            ColPt.cyan(f"1. Add {DISPLY_NAME}")
            payload = {
                "appointment_id": ColPt.input_yellow("Appointment Type: "),
                "total_amount": ColPt.input_yellow("Total Amount: "),
                "payment_status": ColPt.input_yellow("Payment Status: "),
                "payment_type": ColPt.input_yellow("Payment Type: "),
            }
            safe_run(DatabaseAction.add, table_name, payload)

        elif choice == "5":
            ColPt.cyan(f"5. Update {DISPLY_NAME}")
            payload = {
                "billing_id": ColPt.input_yellow("Billing Id: "),
                "appointment_id": ColPt.input_yellow("Appointment Type: "),
                "total_amount": ColPt.input_yellow("Total Amount: "),
                "payment_status": ColPt.input_yellow("Payment Status: "),
                "payment_type": ColPt.input_yellow("Payment Type: "),
            }
            safe_run(DatabaseAction.update, table_name, pri_id_name, payload)

        elif choice == "3":
            ColPt.cyan(f"3. View All {DISPLY_NAME}")
            rows = safe_run(DatabaseAction.get_all, table_name)
            print(tabulate(rows, headers="keys", tablefmt="grid"))

        elif choice == "4":
            ColPt.cyan(f"4. Get {DISPLY_NAME} By ID")
            id = ColPt.input_yellow(f"{DISPLY_NAME} Id: ")
            item = safe_run(DatabaseAction.get_by_id, table_name, pri_id_name, id)
            print(tabulate(item.items(), headers=["Key", "Value"], tablefmt="grid"))

        elif choice == "6":
            ColPt.cyan(f"6. Delete {DISPLY_NAME}")
            id = ColPt.input_yellow(f"{DISPLY_NAME} Id: ")
            safe_run(DatabaseAction.delete, table_name, pri_id_name, id)

        elif choice == "2":
            print("2. Auto-Generate Bill from Treatments")
            print("TASK WIP")

        elif choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
