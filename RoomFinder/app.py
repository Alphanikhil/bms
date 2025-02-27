import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# Configure the app
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_size": 5,  # Optimize connection pool
    "max_overflow": 10,
    "pool_timeout": 30,
    "pool_recycle": 300,
    "pool_pre_ping": True
}

# Initialize the app with the extension
db.init_app(app)

with app.app_context():
    # Import models after db initialization
    from models import Student
    db.create_all()

    # Add sample data if the database is empty
    if not Student.query.first():
        sample_students = [
            Student(
                usn="ITD24AI118",
                name="NIKHIL",
                branch="AIML02",
                room_alloted="BSN 303"
            ),
            Student(
                usn="ITD24AI119",
                name="John Doe",
                branch="AIML02",
                room_alloted="BSN 303"
            ),
            Student(
                usn="ITD24AI120",
                name="Jane Smith",
                branch="AIML02",
                room_alloted="BSN 303"
            )
        ]
        for student in sample_students:
            db.session.add(student)
        db.session.commit()