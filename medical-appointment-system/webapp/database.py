import sqlite3
import os

DB_NAME = "appointments.db"

def get_connection():
    """Create a connection to the SQLite database."""
    db_path = os.path.join(os.path.dirname(__file__), DB_NAME)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # so we can access columns by name
    return conn

def init_db():
    """Create the appointments table if it doesn't exist and add some sample data."""
    conn = get_connection()
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            doctor_name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            reason TEXT
        );
    """)

    # Check if there are already appointments
    cur.execute("SELECT COUNT(*) AS count FROM appointments;")
    row = cur.fetchone()
    count = row["count"]

    # If empty, insert some sample/fake data
    if count == 0:
        sample_data = [
            ("John Doe", "Dr. Smith", "2025-01-15", "10:00", "General check-up"),
            ("Jane Doe", "Dr. Adams", "2025-01-16", "14:30", "Follow-up visit"),
        ]
        cur.executemany("""
            INSERT INTO appointments (patient_name, doctor_name, date, time, reason)
            VALUES (?, ?, ?, ?, ?);
        """, sample_data)

    conn.commit()
    conn.close()

def get_all_appointments():
    """Return all appointments as a list of rows."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM appointments ORDER BY date, time;")
    rows = cur.fetchall()
    conn.close()
    return rows
