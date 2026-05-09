from utils.custome_print import ColPt
from InputHandling.safe_run import safe_run
from modules.department import Department


def department_menu():

    while True:
        ColPt.blue("\n----- Department Management -----")
        print("1. Add Department")
        print("2. View All Department")
        print("3. Get Department By ID")
        print("4. Update Department")
        print("5. Delete Department")
        print("0. Back")

        dept_choice = ColPt.input_yellow("[bold yellow] Enter your choice: ").strip()
        dept = Department()
        if dept_choice == "1":
            print("1. Add Department")

            def _add():
                department_name = ColPt.input_yellow("Department Name: ")
                department_code = ColPt.input_yellow("Department Code: ")
                dept.add(department_name, department_code)

            safe_run(_add)
        elif dept_choice == "2":
            print("2. View All Department")
            rows = safe_run(dept.get_all)
            print(rows)

        elif dept_choice == "3":
            print("3. Get Department By ID")
            department_id = ColPt.input_yellow("Department Id: ")
            item = safe_run(dept.get_by_id, department_id)
            print(item)

        elif dept_choice == "4":
            print("4. Update Department")
            def _update():
                department_id = ColPt.input_yellow("Department Id: ")
                department_name = ColPt.input_yellow("Department Name: ")
                department_code = ColPt.input_yellow("Department Code: ")
                dept.update(department_id, department_name, department_code)

            safe_run(_update)
        elif dept_choice == "5":
            print("5. Delete Department")
            department_id = ColPt.input_yellow("Department Id: ")
            safe_run(dept.delete, department_id)

        elif dept_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
