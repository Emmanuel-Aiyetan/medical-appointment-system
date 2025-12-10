import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Oluwaburna02",
        database="medical_system"
    )
    return conn

def test_connection():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    print("Connected to database:", db_name[0])
    conn.close()

if __name__ == "__main__":
    test_connection()

def insert_sample_data():
    conn = connect_db()
    cursor = conn.cursor()

    # Insert a doctor
    cursor.execute("""
        INSERT INTO doctors (name, specialization, email, phone)
        VALUES (%s, %s, %s, %s)
    """, ("Dr. Smith", "Cardiology", "drsmith@example.com", "555-1234"))

    # Insert a patient
    cursor.execute("""
        INSERT INTO users (name, email, phone, role)
        VALUES (%s, %s, %s, %s)
    """, ("John Doe", "johndoe@example.com", "555-5678", "patient"))

    conn.commit()
    conn.close()
    print("Sample doctor and patient inserted!")

# check what's in the tables
def view_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor.fetchall():
        print(row)
    conn.close()