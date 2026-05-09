from utils.custome_print import ColPt
from InputHandling.safe_run import safe_run
from modules.patient import Patient
from tabulate import tabulate


def patient_menu():

    while True:
        ColPt.blue("\n----- Patient Management -----")
        print("1. Add Patient")
        print("2. View All Patient")
        print("3. Get Patient By ID")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("0. Back")

        pati_choice = ColPt.input_yellow("Enter your choice: ").strip()
        pati = Patient()
        if pati_choice == "1":
            ColPt.cyan("1. Add Patient")
            patient_name = ColPt.input_yellow("Patient Name: ")
            age = ColPt.input_yellow("Age: ")
            gender = ColPt.input_yellow("Gender: ")
            phone_number = ColPt.input_yellow("Phone Number: ")
            address = ColPt.input_yellow("Address: ")

            safe_run(pati.add, patient_name, age, gender, phone_number, address)

        elif pati_choice == "2":
            ColPt.cyan("2. View All Patients")
            rows = safe_run(pati.get_all)
            print(tabulate(rows, headers="keys", tablefmt="grid"))

        elif pati_choice == "3":
            ColPt.cyan("3. Get Patient By ID")
            patient_id = ColPt.input_yellow("Patient Id: ")
            item = safe_run(pati.get_by_id, patient_id)
            print(tabulate(item.items(), headers=["Key", "Value"], tablefmt="grid"))

        elif pati_choice == "4":
            ColPt.cyan("4. Update Patient")
            patient_id = ColPt.input_yellow("Patient Id: ")
            patient_name = ColPt.input_yellow("Patient Name: ")
            age = ColPt.input_yellow("Age: ")
            gender = ColPt.input_yellow("Gender: ")
            phone_number = ColPt.input_yellow("Phone Number: ")
            address = ColPt.input_yellow("Address: ")
            safe_run(pati.update, patient_id, patient_name, age, gender, phone_number, address)

        elif pati_choice == "5":
            ColPt.cyan("5. Delete Patient")
            patient_id = ColPt.input_yellow("Patient Id: ")
            safe_run(pati.delete, patient_id)

        elif pati_choice == "0":
            break
        else:
            ColPt.red("Invalid Choice, Please Try Again!")
