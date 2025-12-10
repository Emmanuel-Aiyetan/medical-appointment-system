from db import connect_db

def register_patient(name, dob, phone, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (name, dob, email, phone, role)
        VALUES (%s, %s, %s, %s, 'patient')
    """, (name, dob, email, phone))
    conn.commit()
    patient_id = cursor.lastrowid
    conn.close()
    return patient_id