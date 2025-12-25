import sqlite3
import os


DB_NAME = "appointments_v2.db"

def get_connection():
    """Create a connection to the SQLite database."""
    db_path = os.path.join(os.path.dirname(__file__), DB_NAME)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # so we can access columns by name
    return conn

def init_db():
    """Create tables if they don't exist and seed basic data."""
    conn = get_connection()
    cur = conn.cursor()

    # Patients table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT
        )
        """
    )

    # Doctors table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialty TEXT
        )
        """
    )

    # Appointments table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            reason TEXT,
            FOREIGN KEY (patient_id) REFERENCES patients(id),
            FOREIGN KEY (doctor_id) REFERENCES doctors(id)
        )
        """
    )

    # Seed sample patients if empty
    cur.execute("SELECT COUNT(*) AS count FROM patients")
    if cur.fetchone()["count"] == 0:
        cur.executemany(
            "INSERT INTO patients (name, email) VALUES (?, ?)",
            [
                ("John Doe", "john@example.com"),
                ("Jane Doe", "jane@example.com"),
            ],
        )

    # Seed sample doctors if empty
    cur.execute("SELECT COUNT(*) AS count FROM doctors")
    if cur.fetchone()["count"] == 0:
        cur.executemany(
            "INSERT INTO doctors (name, specialty) VALUES (?, ?)",
            [
                ("Dr. Smith", "General Practitioner"),
                ("Dr. Adams", "Cardiologist"),
            ],
        )

    conn.commit()
    conn.close()

def get_all_appointments():
    """All appointments with joined patient/doctor names."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT a.id,
               p.name AS patient_name,
               d.name AS doctor_name,
               a.date,
               a.time,
               a.reason
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
        ORDER BY a.date, a.time
        """
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def get_all_patients():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients ORDER BY name")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_all_doctors():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctors ORDER BY name")
    rows = cur.fetchall()
    conn.close()
    return rows

def create_patient(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO patients (name, email) VALUES (?, ?)",
        (name, email),
    )
    conn.commit()
    conn.close()

def create_doctor(name, specialty):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO doctors (name, specialty) VALUES (?, ?)",
        (name, specialty),
    )
    conn.commit()
    conn.close()

def create_appointment(patient_id, doctor_id, date, time, reason):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO appointments (patient_id, doctor_id, date, time, reason)
        VALUES (?, ?, ?, ?, ?)
        """,
        (patient_id, doctor_id, date, time, reason),
    )
    conn.commit()
    conn.close()

def get_appointments_for_patient(patient_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT a.id,
               p.name AS patient_name,
               d.name AS doctor_name,
               a.date,
               a.time,
               a.reason
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
        WHERE p.id = ?
        ORDER BY a.date, a.time
        """,
        (patient_id,),
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def get_appointments_for_doctor(doctor_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT a.id,
               p.name AS patient_name,
               d.name AS doctor_name,
               a.date,
               a.time,
               a.reason
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
        WHERE d.id = ?
        ORDER BY a.date, a.time
        """,
        (doctor_id,),
    )
    rows = cur.fetchall()
    conn.close()
    return rows
