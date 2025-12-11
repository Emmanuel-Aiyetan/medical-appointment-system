from db import connect_db

def register_doctor(name, specialization):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO doctors (name, specialization)
        VALUES (%s, %s)
    """, (name, specialization))
    conn.commit()
    doctor_id = cursor.lastrowid
    conn.close()
    return doctor_id

def view_doctor_schedule(doctor_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.appointment_id, p.name, a.appointment_date, a.status
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        WHERE a.doctor_id = %s
        ORDER BY a.appointment_date
    """, (doctor_id,))
    results = cursor.fetchall()
    conn.close()

    if not results:
        print(" No appointments scheduled.")
    else:
        print("\n=== Doctor's Schedule ===")
        for row in results:
            print(f"Appointment {row[0]} | Patient: {row[1]} | Date: {row[2]} | Status: {row[3]}")