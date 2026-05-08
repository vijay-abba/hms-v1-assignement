from rich.console import Console

console = Console()


def doctor_menu():
    while True:
        console.print("\n----- Doctor Management -----", style="bold blue")
        print("1. Add Doctor")
        print("2. View All Doctor")
        print("3. Get Doctor By ID")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("0. Back")

        doc_choice = console.input("[bold yellow] Enter your choice: ").strip()

        if doc_choice == "1":
            print("1. Add Doctor")
        elif doc_choice == "2":
            print("2. View All Doctor")
        elif doc_choice == "3":
            print("3. Get Doctor By ID")
        elif doc_choice == "4":
            print("4. Update Doctor")
        elif doc_choice == "5":
            print("5. Delete Doctor")
        elif doc_choice == "0":
            break
        else:
            console.print("Invalid Choice, Please Try Again!", style="bold red")
