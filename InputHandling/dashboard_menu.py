from utils.custome_print import ColPt
from modules.dashboard import Dashboard
from InputHandling.safe_run import safe_run
from tabulate import tabulate


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
            ColPt.cyan("1. Summary Numbers")
            rows = safe_run(Dashboard.summary, "1")
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        elif dash_choice == "2":
            ColPt.cyan("2. Top Doctors by Revenue")
            rows = safe_run(Dashboard.summary, "2")
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        elif dash_choice == "3":
            ColPt.cyan("3. Patients per department")
            rows = safe_run(Dashboard.summary, "3")
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        elif dash_choice == "4":
            ColPt.cyan("4. Monthly Revenue Trend")
            rows = safe_run(Dashboard.summary, "4")
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        elif dash_choice == "5":
            ColPt.cyan("5. Pending payments")
            rows = safe_run(Dashboard.summary, "5")
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        elif dash_choice == "6":
            ColPt.cyan("6. Most common treatments")
            rows = safe_run(Dashboard.summary, "6")
            print(tabulate(rows, headers="keys", tablefmt="grid"))
        elif dash_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
