from datetime import datetime


appointments = {}

next_id = 101

doctors = ["Dr. Mehta", "Dr. Rao"]



def is_slot_available(doctor, date, time, ignore_id=None):

    for appointment_id, details in appointments.items():

        if appointment_id == ignore_id:
            continue

        if (details["doctor"] == doctor
                and details["date"] == date
                and details["time"] == time):
            return False

    return True



def get_valid_date_time():

    date = input("Enter Date (DD-MM-YYYY): ")
    time = input("Enter Time (HH:MM): ")

    try:
        date_obj = datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return None, None

    try:
        time_obj = datetime.strptime(time, "%H:%M")
    except ValueError:
        print("Invalid time. Please enter the time as HH:MM.")
        return None, None

    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("16:30", "%H:%M")

    if time_obj < start_time or time_obj > end_time:
        print("Appointment time must be between 09:00 and 16:30.")
        return None, None

    if time_obj.minute not in [0, 30]:
        print("Only 30-minute slots are allowed.")
        return None, None

    return date_obj.strftime("%d-%m-%Y"), time_obj.strftime("%H:%M")


def book_appointment():

    global next_id

    patient = input("Enter Patient Name: ")

    if patient.strip() == "":
        print("Patient name cannot be empty.")
        return

    doctor = input("Enter Doctor (Dr. Mehta / Dr. Rao): ")

    if doctor not in doctors:
        print("Invalid doctor name.")
        return

    date, time = get_valid_date_time()

    if date is None:
        return

    if not is_slot_available(doctor, date, time):
        print("Slot unavailable:", doctor,
              "already has an appointment at this time.")
        return

    appointment_id = "A" + str(next_id)

    appointments[appointment_id] = {
        "patient": patient,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    print("Appointment booked.")
    print("ID:", appointment_id, "|", patient, "|",
          doctor, "|", date, time)

    next_id += 1


def view_appointments():

    if len(appointments) == 0:
        print("No appointments found.")
        return

    print("\n----- ALL APPOINTMENTS -----")

    for appointment_id, details in appointments.items():

        print(
            appointment_id, "|",
            details["patient"], "|",
            details["doctor"], "|",
            details["date"], details["time"]
        )

    print("Total appointments:", len(appointments))



def reschedule_appointment():

    appointment_id = input("Enter Appointment ID: ").upper()

    if appointment_id not in appointments:
        print("Appointment ID not found.")
        return

    doctor = appointments[appointment_id]["doctor"]

    print("Enter new appointment details:")

    date, time = get_valid_date_time()

    if date is None:
        return

    if not is_slot_available(
        doctor, date, time, appointment_id
    ):
        print("New slot is unavailable.")
        return

    appointments[appointment_id]["date"] = date
    appointments[appointment_id]["time"] = time

    print(
        "Appointment", appointment_id,
        "rescheduled to", date, time
    )


def cancel_appointment():

    appointment_id = input("Enter Appointment ID: ").upper()

    if appointment_id in appointments:

        del appointments[appointment_id]

        print("Appointment", appointment_id, "cancelled.")

    else:
        print("Appointment ID not found.")



def main():

    while True:

        print("\n===== HOSPITAL APPOINTMENT SCHEDULER =====")
        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. Reschedule Appointment")
        print("4. Cancel Appointment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_appointment()

        elif choice == "2":
            view_appointments()

        elif choice == "3":
            reschedule_appointment()

        elif choice == "4":
            cancel_appointment()

        elif choice == "5":
            print("Thank you for using Hospital Appointment Scheduler.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()