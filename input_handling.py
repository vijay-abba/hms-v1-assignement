from utils.custome_print import ColPt
from InputHandling.safe_run import safe_run
from db_action import DatabaseAction
from tabulate import tabulate


class InputHandling:

    def __init__(self, DISPLY_NAME, table_name, pri_id_name, fields):
        self.DISPLY_NAME = DISPLY_NAME
        self.table_name = table_name
        self.pri_id_name = pri_id_name
        self.fields = fields

    def print_options(self):
        ColPt.blue(f"\n----- {self.DISPLY_NAME} Management -----")
        add_text = "BooK" if self.DISPLY_NAME == "Appointment" else "Add"
        print(f"1. {add_text} {self.DISPLY_NAME}")
        print(f"2. View All {self.DISPLY_NAME}s")
        print(f"3. Get {self.DISPLY_NAME} By ID")
        print(f"4. Update {self.DISPLY_NAME}")
        print(f"5. Delete {self.DISPLY_NAME}")
        print(f"0. Back")

    def selected_add(self):
        ColPt.cyan(f"1. Add {self.DISPLY_NAME}")
        payload = {}
        for key, val in self.fields.items():
            if key == self.pri_id_name:
                continue
            payload[key] = ColPt.input_yellow(f"{val}: ")
        safe_run(DatabaseAction.add, self.table_name, payload)

    def selected_update(self):
        ColPt.cyan(f"4. Update {self.DISPLY_NAME}")
        payload = {}
        for key, val in self.fields.items():
            payload[key] = ColPt.input_yellow(f"{val}: ")
        safe_run(DatabaseAction.update, self.table_name, self.pri_id_name, payload)

    def selected_view_all(self):
        ColPt.cyan(f"2. View All {self.DISPLY_NAME}")
        rows = safe_run(DatabaseAction.get_all, self.table_name)
        print(tabulate(rows, headers="keys", tablefmt="grid"))

    def selected_get_by_id(self):
        ColPt.cyan(f"3. Get {self.DISPLY_NAME} By ID")
        id = ColPt.input_yellow(f"{self.DISPLY_NAME} Id: ")
        item = safe_run(DatabaseAction.get_by_id, self.table_name, self.pri_id_name, id)
        print(tabulate(item.items(), headers=["Key", "Value"], tablefmt="grid"))

    def selected_delete(self):
        ColPt.cyan(f"5. Delete {self.DISPLY_NAME}")
        id = ColPt.input_yellow(f"{self.DISPLY_NAME} Id: ")
        safe_run(DatabaseAction.delete, self.table_name, self.pri_id_name, id)

    def run_process(self):

        while True:
            self.print_options()

            choice = ColPt.input_yellow("Enter your choice: ").strip()

            # fmt: off
            if choice == "1": self.selected_add()
            elif choice == "2": self.selected_view_all()
            elif choice == "3": self.selected_get_by_id()
            elif choice == "4": self.selected_update()
            elif choice == "5": self.selected_delete()
            elif choice == "0":
                break
            else:
                ColPt.red("Invalid Choice, Please Try Again!")
            # fmt on


class InputHandlingBill(InputHandling):

    def __init__(self, DISPLY_NAME, table_name, pri_id_name, fields):
        super().__init__(DISPLY_NAME, table_name, pri_id_name, fields)

    def print_options(self):
        ColPt.blue(f"\n----- {self.DISPLY_NAME} Management -----")
        print(f"1. Add {self.DISPLY_NAME} (manual)")
        print("2. Auto-Generate Bill from Treatments")
        print(f"3. View All {self.DISPLY_NAME}s")
        print(f"4. Get {self.DISPLY_NAME} By ID")
        print(f"5. Update {self.DISPLY_NAME}")
        print(f"6. Delete {self.DISPLY_NAME}")
        print(f"0. Back")


    def auto_generate_bill(self):
        print("Auto Generate Bill")
        #3Auto-Generate Bill from Treatments
    

    def run_process(self):

        while True:
            self.print_options()

            choice = ColPt.input_yellow("Enter your choice: ").strip()

            # fmt: off
            if choice == "1": self.selected_add()
            elif choice == "2": self.auto_generate_bill()
            elif choice == "3": self.selected_view_all()
            elif choice == "4": self.selected_get_by_id()
            elif choice == "5": self.selected_update()
            elif choice == "6": self.selected_delete()
            elif choice == "0":
                break
            else:
                ColPt.red("Invalid Choice, Please Try Again!")
            # fmt on
