import datetime

class Patient:
    def __init__(self, patient_id, name, dob, contact):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob  # Date of Birth (e.g., "YYYY-MM-DD")
        self.contact = contact
        self.medical_history = []

    def add_medical_record(self, record):
        self.medical_history.append(record)

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Contact: {self.contact}"

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_name, date_time, purpose):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_name = doctor_name
        self.date_time = date_time # datetime object
        self.purpose = purpose
        self.status = "Scheduled"

    def __str__(self):
        return (f"Appointment ID: {self.appointment_id}, Patient ID: {self.patient_id}, "
                f"Doctor: {self.doctor_name}, Time: {self.date_time.strftime('%Y-%m-%d %H:%M')}, "
                f"Purpose: {self.purpose}, Status: {self.status}")

class ClinicManagementSystem:
    def __init__(self):
        self.patients = {}  # patient_id: Patient object
        self.appointments = {} # appointment_id: Appointment object
        self.next_patient_id = 1
        self.next_appointment_id = 1

    def register_patient(self, name, dob, contact):
        patient_id = f"P{self.next_patient_id:04d}"
        patient = Patient(patient_id, name, dob, contact)
        self.patients[patient_id] = patient
        self.next_patient_id += 1
        print(f"Patient {name} registered with ID: {patient_id}")
        return patient_id

    def schedule_appointment(self, patient_id, doctor_name, date_time_str, purpose):
        if patient_id not in self.patients:
            print(f"Error: Patient with ID {patient_id} not found.")
            return None
        
        try:
            date_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        except ValueError:
            print("Error: Invalid date/time format. Use YYYY-MM-DD HH:MM")
            return None

        appointment_id = f"A{self.next_appointment_id:04d}"
        appointment = Appointment(appointment_id, patient_id, doctor_name, date_time, purpose)
        self.appointments[appointment_id] = appointment
        self.next_appointment_id += 1
        print(f"Appointment scheduled for {self.patients[patient_id].name} with Dr. {doctor_name} on {date_time_str}")
        return appointment_id

    def view_patient_appointments(self, patient_id):
        if patient_id not in self.patients:
            print(f"Error: Patient with ID {patient_id} not found.")
            return

        print(f"\n--- Appointments for {self.patients[patient_id].name} ---")
        found_appointments = False
        for app_id, app in self.appointments.items():
            if app.patient_id == patient_id:
                print(app)
                found_appointments = True
        if not found_appointments:
            print("No appointments found for this patient.")

    def list_all_patients(self):
        print("\n--- All Registered Patients ---")
        if not self.patients:
            print("No patients registered yet.")
            return
        for patient_id, patient in self.patients.items():
            print(patient)

# --- How to use it (Basic CLI interaction) ---
if __name__ == "__main__":
    cms = ClinicManagementSystem()

    while True:
        print("\n--- Clinic Management System ---")
        print("1. Register Patient")
        print("2. Schedule Appointment")
        print("3. View Patient Appointments")
        print("4. List All Patients")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient name: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            contact = input("Enter contact number: ")
            cms.register_patient(name, dob, contact)
        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            doctor_name = input("Enter doctor's name: ")
            date_time_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            purpose = input("Enter purpose of appointment: ")
            cms.schedule_appointment(patient_id, doctor_name, date_time_str, purpose)
        elif choice == '3':
            patient_id = input("Enter patient ID: ")
            cms.view_patient_appointments(patient_id)
        elif choice == '4':
            cms.list_all_patients()
        elif choice == '5':
            print("Exiting Clinic Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")s