from hospital_management import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=False)
    first_name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    other_name = db.Column(db.String(120), unique=False, nullable=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    nationality = db.Column(db.String(120), unique=False, nullable=False)
    country = db.Column(db.String(120), unique=False, nullable=False)
    country_code = db.Column(db.String(120), unique=False, nullable=False)
    city = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=True)
    phone_no = db.Column(db.String(120), unique=False, nullable=True)
    date_of_birth = db.Column(db.DateTime(120), unique=False, nullable=False)
    date_created = db.Column(db.DateTime(120), default=datetime.utcnow())
    mypatient = db.relationship('Patient', backref='doctor', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120), unique=False, nullable=False)
    lastName = db.Column(db.String(120), unique=False, nullable=False)
    otherName = db.Column(db.String(120), unique=False, nullable=False)
    patientAge = db.Column(db.String(120), unique=False, nullable=False)
    ailment = db.Column(db.String(120), unique=False, nullable=False)
    bloodGroup = db.Column(db.String(120), unique=False, nullable=False)
    genoType = db.Column(db.String(120), unique=False, nullable=False)
    addressPatient = db.Column(db.String(120), unique=False, nullable=False)
    cityPatient = db.Column(db.String(120), unique=False, nullable=False)
    statePatient = db.Column(db.String(120), unique=False, nullable=False)
    countryPatient = db.Column(db.String(120), unique=False, nullable=False)
    phone_noPatient = db.Column(db.String(120), unique=False, nullable=False)
    
    nameOfKin = db.Column(db.String(120), unique=False, nullable=False)
    addressOfKin = db.Column(db.String(120), unique=False, nullable=False)
    cityOfKin = db.Column(db.String(120), unique=False, nullable=False)
    stateOfKin = db.Column(db.String(120), unique=False, nullable=False)
    countryOfKin = db.Column(db.String(120), unique=False, nullable=False)
    phoneNoOfKin = db.Column(db.String(120), unique=False, nullable=False)
    date_created = db.Column(db.DateTime(120), default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)