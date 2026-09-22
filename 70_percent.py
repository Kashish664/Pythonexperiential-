# Hospital Management System - 70% Version
patients = []
doctors = []
appointments = []
bills = []

def add_patient():
    pid = input("Patient ID: ")
    name = input("Patient Name: ")
    age = input("Age: ")
    patients.append({"id": pid, "name": name, "age": age})
    print("Patient added successfully!")

def add_doctor():
    did = input("Doctor ID: ")
    name = input("Doctor Name: ")
    spec = input("Specialization: ")
    doctors.append({"id": did, "name": name, "specialization": spec})
    print("Doctor added successfully!")

def book_appointment():
    pid = input("Patient ID: ")
    did = input("Doctor ID: ")
    date = input("Date: ")
    appointments.append({"patient": pid, "doctor": did, "date": date})
    print("Appointment booked successfully!")

def generate_bill():
    pid = input("Patient ID: ")
    amount = float(input("Bill Amount: "))
    bills.append({"patient": pid, "amount": amount})
    print("Bill generated successfully!")

def view_records():
    print("\n--- Patients ---")
    for p in patients:
        print(p)
    print("\n--- Doctors ---")
    for d in doctors:
        print(d)
    print("\n--- Appointments ---")
    for a in appointments:
        print(a)
    print("\n--- Bills ---")
    for b in bills:
        print(b)

while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Book Appointment")
    print("4. Generate Bill")
    print("5. View Records")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        generate_bill()
    elif choice == "5":
        view_records()
    elif choice == "6":
        print("Thank you! System closed.")
        break
    else:
        print("Invalid choice!")
