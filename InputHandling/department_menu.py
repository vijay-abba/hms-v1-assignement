from utils.custome_print import ColPt
from InputHandling.safe_run import safe_run
from modules.department import Department
from tabulate import tabulate


def department_menu():

    while True:
        ColPt.blue("\n----- Department Management -----")
        print("1. Add Department")
        print("2. View All Department")
        print("3. Get Department By ID")
        print("4. Update Department")
        print("5. Delete Department")
        print("0. Back")

        dept_choice = ColPt.input_yellow("Enter your choice: ").strip()
        dept = Department()
        if dept_choice == "1":
            ColPt.cyan("1. Add Department")
            department_name = ColPt.input_yellow("Department Name: ")
            department_code = ColPt.input_yellow("Department Code: ")
            safe_run(dept.add, department_name, department_code)

        elif dept_choice == "2":
            ColPt.cyan("2. View All Department")
            rows = safe_run(dept.get_all)
            print(tabulate(rows, headers="keys", tablefmt="grid"))

        elif dept_choice == "3":
            ColPt.cyan("3. Get Department By ID")
            department_id = ColPt.input_yellow("Department Id: ")
            item = safe_run(dept.get_by_id, department_id)
            print(tabulate(item.items(), headers=["Key", "Value"], tablefmt="grid"))

        elif dept_choice == "4":
            ColPt.cyan("4. Update Department")
            department_id = ColPt.input_yellow("Department Id: ")
            department_name = ColPt.input_yellow("Department Name: ")
            department_code = ColPt.input_yellow("Department Code: ")
            safe_run(dept.update, department_id, department_name, department_code)

        elif dept_choice == "5":
            ColPt.cyan("5. Delete Department")
            department_id = ColPt.input_yellow("Department Id: ")
            safe_run(dept.delete, department_id)

        elif dept_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
