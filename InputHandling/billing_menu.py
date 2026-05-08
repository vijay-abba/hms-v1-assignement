

from rich.console import Console

console = Console()


def billing_menu():
    while True:
        console.print("\n----- Billing Management -----", style="bold blue")
        print("1. Add Bill (manual)")
        print("2. Auto-Generate Bill from Treatments")
        print("3. View All Bills")
        print("4. Get Bill by ID")
        print("5. Update Bill")
        print("6. Delete Bill")
        print("0. Back")


        bill_choice = console.input("[bold yellow] Enter your choice: ").strip()

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
            console.print("Invalid Choice, Please Try Again!", style="bold red")

