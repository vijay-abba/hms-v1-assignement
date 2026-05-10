from utils.custome_print import ColPt
from InputHandling.safe_run import safe_run
from tabulate import tabulate
from db_action import DatabaseAction


def treatment_menu():

    # TASK: PENDING DOC
    DISPLY_NAME = "Treatment"
    table_name = "treatment"
    pri_id_name = "treatment_id"

    while True:
        ColPt.blue(f"\n----- {DISPLY_NAME} Management -----")
        print(f"1. Add {DISPLY_NAME}")
        print(f"2. View All {DISPLY_NAME}s")
        print(f"3. Get {DISPLY_NAME} By ID")
        print(f"4. Update {DISPLY_NAME}")
        print(f"5. Delete {DISPLY_NAME}")
        print("6. View Treatments By Appointment")
        print(f"0. Back")

        choice = ColPt.input_yellow("Enter your choice: ").strip()

        if choice == "1":
            ColPt.cyan(f"1. Add {DISPLY_NAME}")
            payload = {
                "treatment_type": ColPt.input_yellow("Treatment Type: "),
                "appointment_id": ColPt.input_yellow("Appointment Id: "),
                "cost": ColPt.input_yellow("cost: "),
            }
            safe_run(DatabaseAction.add, table_name, payload)

        elif choice == "4":
            ColPt.cyan(f"4. Update {DISPLY_NAME}")
            payload = {
                "treatment_id": ColPt.input_yellow("Treatment Id: "),
                "treatment_type": ColPt.input_yellow("Treatment Type: "),
                "appointment_id": ColPt.input_yellow("Appointment Id: "),
                "cost": ColPt.input_yellow("cost: "),
            }
            safe_run(DatabaseAction.update, table_name, pri_id_name, payload)

        elif choice == "2":
            ColPt.cyan(f"2. View All {DISPLY_NAME}")
            rows = safe_run(DatabaseAction.get_all, table_name)
            print(tabulate(rows, headers="keys", tablefmt="grid"))

        elif choice == "3":
            ColPt.cyan(f"3. Get {DISPLY_NAME} By ID")
            id = ColPt.input_yellow(f"{DISPLY_NAME} Id: ")
            item = safe_run(DatabaseAction.get_by_id, table_name, pri_id_name, id)
            print(tabulate(item.items(), headers=["Key", "Value"], tablefmt="grid"))

        elif choice == "5":
            ColPt.cyan(f"5. Delete {DISPLY_NAME}")
            id = ColPt.input_yellow(f"{DISPLY_NAME} Id: ")
            safe_run(DatabaseAction.delete, table_name, pri_id_name, id)

        elif choice == "6":
            print("6. View Treatments By Appointment")
            print("TASK WIP")

        elif choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
