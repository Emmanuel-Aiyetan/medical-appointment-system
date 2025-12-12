from flask import Flask, render_template
from database import init_db, get_all_appointments

app = Flask(__name__)

# Initialize the database when the app starts
init_db()

@app.route("/")
def home():
    appointments = get_all_appointments()
    return render_template("home.html", appointments=appointments)

if __name__ == "__main__":
    app.run(debug=True)
    