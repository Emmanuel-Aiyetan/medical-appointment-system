from patients import register_patient
from doctors import register_doctor, view_doctor_schedule
from appointments import book_appointment, view_patient_appointments

def main_menu():
    print("\n=== Medical Appointment System ===")
    print("1. Register as new patient")
    print("2. Book an appointment (Patient)")
    print("3. View my appointments (Patient)")
    print("4. Register as new doctor")
    print("5. View my schedule (Doctor)")
    print("6. Exit")
    return input("Enter your choice: ")

def run_app():
    patient_id = None
    doctor_id = None

    while True:
        choice = main_menu()

        if choice == "1":
            name = input("Enter your full name: ")
            dob = input("Enter your date of birth (YYYY-MM-DD): ")
            phone = input("Enter your phone number: ")
            email = input("Enter your email: ")
            patient_id = register_patient(name, dob, phone, email)
            print(f" Patient registered! Your Patient ID is {patient_id}")

        elif choice == "2":
            if not patient_id:
                patient_id = int(input("Enter your Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            appointment_date = input("Enter appointment date (YYYY-MM-DD HH:MM:SS): ")
            book_appointment(patient_id, doctor_id, appointment_date)

        elif choice == "3":
            if not patient_id:
                patient_id = int(input("Enter your Patient ID: "))
            view_patient_appointments(patient_id)

        elif choice == "4":
            name = input("Enter Doctor Name: ")
            specialization = input("Enter Specialization: ")
            doctor_id = register_doctor(name, specialization)
            print(f" Doctor registered! Your Doctor ID is {doctor_id}")

        elif choice == "5":
            if not doctor_id:
                doctor_id = int(input("Enter your Doctor ID: "))
            view_doctor_schedule(doctor_id)

        elif choice == "6":
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    run_app()
