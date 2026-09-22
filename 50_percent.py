# Hospital Management System - 50% Version
patients = []
doctors = []

def add_patient():
    pid = input("Patient ID: ")
    name = input("Patient Name: ")
    patients.append({"id": pid, "name": name})
    print("Patient added!")

def add_doctor():
    did = input("Doctor ID: ")
    name = input("Doctor Name: ")
    doctors.append({"id": did, "name": name})
    print("Doctor added!")

def view_data():
    print("Patients:", patients)
    print("Doctors:", doctors)

while True:
    print("\n1.Add Patient  2.Add Doctor  3.View  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        view_data()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
