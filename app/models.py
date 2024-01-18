# app/models.py
from flask_sqlalchemy import SQLAlchemy
from . import db

# db = SQLAlchemy()

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    round_number = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __repr__(self):
        return f'<Candidate {self.name}>'
