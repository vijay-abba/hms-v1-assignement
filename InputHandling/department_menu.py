from utils.custome_print import ColPt
from InputHandling.safe_run import safe_run

# from modules.department import Department
from tabulate import tabulate
from db_action import DatabaseAction


def department_menu():

    DISPLY_NAME = "Department"
    table_name = "departments"
    pri_id_name = "department_id"

    while True:
        ColPt.blue(f"\n----- {DISPLY_NAME} Management -----")
        print(f"1. Add {DISPLY_NAME}")
        print(f"2. View All {DISPLY_NAME}")
        print(f"3. Get {DISPLY_NAME} By ID")
        print(f"4. Update {DISPLY_NAME}")
        print(f"5. Delete {DISPLY_NAME}")
        print(f"0. Back")

        department_choice = ColPt.input_yellow("Enter your choice: ").strip()

        if department_choice == "1":
            ColPt.cyan(f"1. Add {DISPLY_NAME}")
            payload = {
                "department_name": ColPt.input_yellow("Department Name: "),
                "department_code": ColPt.input_yellow("Department Code: "),
            }
            safe_run(DatabaseAction.add, table_name, payload)

        elif department_choice == "2":
            ColPt.cyan(f"2. View All {DISPLY_NAME}")
            rows = safe_run(DatabaseAction.get_all, table_name)
            print(tabulate(rows, headers="keys", tablefmt="grid"))

        elif department_choice == "3":
            ColPt.cyan(f"3. Get {DISPLY_NAME} By ID")
            department_id = ColPt.input_yellow("Department Id: ")
            item = safe_run(
                DatabaseAction.get_by_id, table_name, pri_id_name, department_id
            )
            print(tabulate(item.items(), headers=["Key", "Value"], tablefmt="grid"))

        elif department_choice == "4":
            ColPt.cyan(f"4. Update {DISPLY_NAME}")
            payload = {
                "department_id": ColPt.input_yellow("Department Id: "),
                "department_name": ColPt.input_yellow("Department Name: "),
                "department_code": ColPt.input_yellow("Department Code: "),
            }
            safe_run(DatabaseAction.update, table_name, pri_id_name, payload)

        elif department_choice == "5":
            ColPt.cyan(f"5. Delete {DISPLY_NAME}")
            department_id = ColPt.input_yellow("Department Id: ")
            safe_run(DatabaseAction.delete, table_name, pri_id_name, department_id)

        elif department_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
