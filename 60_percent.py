# Hospital Management System - 60% Version
patients = []
doctors = []
appointments = []

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

def book_appointment():
    pid = input("Patient ID: ")
    did = input("Doctor ID: ")
    date = input("Appointment Date: ")
    appointments.append({"patient": pid, "doctor": did, "date": date})
    print("Appointment booked!")

def view_all():
    print("\nPatients:", patients)
    print("Doctors:", doctors)
    print("Appointments:", appointments)

while True:
    print("\n1.Patient  2.Doctor  3.Appointment  4.View All  5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("System closed.")
        break
    else:
        print("Invalid choice!")
