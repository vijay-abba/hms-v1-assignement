from utils.custome_print import ColPt
from InputHandling.safe_run import safe_run
from tabulate import tabulate
from db_action import DatabaseAction


def doctor_menu():

    DISPLY_NAME = "Patient"
    table_name = "patients"
    pri_id_name = "patient_id"

    while True:
        ColPt.blue(f"\n----- {DISPLY_NAME} Management -----")
        print(f"1. Add {DISPLY_NAME}")
        print(f"2. View All {DISPLY_NAME}")
        print(f"3. Get {DISPLY_NAME} By ID")
        print(f"4. Update {DISPLY_NAME}")
        print(f"5. Delete {DISPLY_NAME}")
        print(f"0. Back")

        patient_choice = ColPt.input_yellow("Enter your choice: ").strip()

        if patient_choice == "1":
            ColPt.cyan(f"1. Add {DISPLY_NAME}")
            payload = {
                "patient_name": ColPt.input_yellow("Patient Name: "),
                "age": ColPt.input_yellow("Age: "),
                "gender": ColPt.input_yellow("Gender: "),
                "phone_number": ColPt.input_yellow("Phone Number: "),
                "address": ColPt.input_yellow("Address: "),
            }
            safe_run(DatabaseAction.add, table_name, payload)

        elif patient_choice == "2":
            ColPt.cyan(f"2. View All {DISPLY_NAME}")
            rows = safe_run(DatabaseAction.get_all, table_name)
            print(tabulate(rows, headers="keys", tablefmt="grid"))

        elif patient_choice == "3":
            ColPt.cyan(f"3. Get {DISPLY_NAME} By ID")
            patient_id = ColPt.input_yellow("Patient Id: ")
            item = safe_run(
                DatabaseAction.get_by_id, table_name, pri_id_name, patient_id
            )
            print(tabulate(item.items(), headers=["Key", "Value"], tablefmt="grid"))

        elif patient_choice == "4":
            ColPt.cyan(f"4. Update {DISPLY_NAME}")
            payload = {
                "patient_id": ColPt.input_yellow("Patient Id: "),
                "patient_name": ColPt.input_yellow("Patient Name: "),
                "age": ColPt.input_yellow("Age: "),
                "gender": ColPt.input_yellow("Gender: "),
                "phone_number": ColPt.input_yellow("Phone Number: "),
                "address": ColPt.input_yellow("Address: "),
            }
            safe_run(DatabaseAction.update, table_name, pri_id_name, payload)

        elif patient_choice == "5":
            ColPt.cyan(f"5. Delete {DISPLY_NAME}")
            patient_id = ColPt.input_yellow("Patient Id: ")
            safe_run(DatabaseAction.delete, table_name, pri_id_name, patient_id)

        elif patient_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
