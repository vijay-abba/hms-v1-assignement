from rich.console import Console

console = Console()


def patient_menu():
    while True:
        console.print("\n----- Patient Management -----", style="bold blue")
        print("1. Add Patient")
        print("2. View All Patient")
        print("3. Get Patient By ID")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("0. Back")

        pat_choice = console.input("[bold yellow] Enter your choice: ").strip()

        if pat_choice == "1":
            print("1. Add Patient")
        elif pat_choice == "2":
            print("2. View All Patient")
        elif pat_choice == "3":
            print("3. Get Patient By ID")
        elif pat_choice == "4":
            print("4. Update Patient")
        elif pat_choice == "5":
            print("5. Delete Patient")
        elif pat_choice == "0":
            break
        else:
            console.print("Invalid Choice, Please Try Again!", style="bold red")
