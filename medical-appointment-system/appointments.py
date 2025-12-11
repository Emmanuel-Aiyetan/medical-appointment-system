from db import connect_db

def book_appointment(user_id, doctor_id, date_time):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO appointments (user_id, doctor_id, appointment_date)
        VALUES (%s, %s, %s)
    """, (user_id, doctor_id, date_time))
    conn.commit()
    conn.close()
    print("✅ Appointment booked successfully!")

def view_patient_appointments(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.appointment_id, d.name, d.specialization, a.appointment_date, a.status
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE a.user_id = %s
        ORDER BY a.appointment_date;
    """, (user_id,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("\n📭 No appointments found.")
    else:
        print("\n📅 Your Appointments:")
        for row in rows:
            print(f"ID: {row[0]} | Doctor: {row[1]} ({row[2]}) | Date: {row[3]} | Status: {row[4]}")
