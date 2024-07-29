from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.String(10), nullable=False)
    from_city = db.Column(db.String(50), nullable=False)
    to_city = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default="Scheduled")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('flights', lazy=True))
