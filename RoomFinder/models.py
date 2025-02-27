from app import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(20), unique=True, nullable=False, index=True)  # Added index
    name = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(50), nullable=False)
    room_alloted = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Student {self.usn}>'

    def to_dict(self):
        return {
            'usn': self.usn,
            'name': self.name,
            'branch': self.branch,
            'room_alloted': self.room_alloted
        }