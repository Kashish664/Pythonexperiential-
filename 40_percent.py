# Hospital Management System - 40% Version
patients = []

def add_patient():
    name = input("Enter patient name: ")
    patients.append(name)
    print("Patient added successfully!")

def view_patients():
    print("Patients:", patients)

while True:
    print("\n1. Add Patient\n2. View Patients\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        print("System closed.")
        break
    else:
        print("Invalid choice!")
