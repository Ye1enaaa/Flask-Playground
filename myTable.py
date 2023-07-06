from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MyTable(db.Model):
    __tablename__ = 'mytable'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

class CalculateGrams(db.Model):
    __tablename__ = 'calculategrams'
    id = db.Column(db.Integer, primary_key=True)
    grams = db.Column(db.Integer())