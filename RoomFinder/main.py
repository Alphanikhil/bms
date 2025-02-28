from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import logging
import json
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Define the path to the data.json file
DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.json')

def load_students():
    """Load students from JSON file."""
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            data = json.load(f)
            logging.debug(f"Loaded students: {data.get('students', [])}")
            return data.get('students', [])
    except FileNotFoundError:
        logging.error("data.json file not found")
        return []

def save_students(students):
    """Save students to JSON file."""
    with open(DATA_FILE_PATH, 'w') as f:
        json.dump({'students': students}, f, indent=2)

def validate_usn(usn):
    """Validate USN format."""
    return bool(usn and usn.strip())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usn = request.form.get('usn', '').strip().upper()
        logging.debug(f"Received USN: {usn}")

        if not validate_usn(usn):
            flash('Please enter your USN', 'danger')
        else:
            students = load_students()
            student = next((s for s in students if s['usn'] == usn), None)
            logging.debug(f"Found student: {student}")
            if student:
                return redirect(url_for('student_details', usn=usn))
            else:
                flash('No student found with the given USN', 'warning')

    return render_template('index.html')

@app.route('/student/<usn>')
def student_details(usn):
    students = load_students()
    student = next((s for s in students if s['usn'] == usn), None)
    if student:
        return render_template('student_details.html', student=student)
    flash('Student not found', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Get port from environment variable or default to 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
