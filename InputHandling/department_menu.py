from rich.console import Console

console = Console()


def department_menu():
    while True:
        console.print("\n----- Department Management -----", style="bold blue")
        print("1. Add Department")
        print("2. View All Department")
        print("3. Get Department By ID")
        print("4. Update Department")
        print("5. Delete Department")
        print("0. Back")

        dept_choice = user_choice = console.input("[bold yellow] Enter your choice: ")

        if dept_choice == "1":
            print("1. Add Department")
        elif dept_choice == "2":
            print("2. View All Department")
        elif dept_choice == "3":
            print("3. Get Department By ID")
        elif dept_choice == "4":
            print("4. Update Department")
        elif dept_choice == "5":
            print("5. Delete Department")
        elif dept_choice == "0":
            break
        else:
            console.print("Invalid Choice, Please Try Again!", style="bold red")
