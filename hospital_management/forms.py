from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField, PasswordField, SubmitField, DateField, IntegerField, TelField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Optional
from hospital_management.utils import countries_data
from hospital_management.countries_api import countries

title = ['Mr', 'Miss', 'Mrs', 'Dr Mr', 'Dr Miss', 'Dr Mrs']

class RegisterForm(FlaskForm):
    title = SelectField('Title', choices=title, validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=120)])
    last_name = StringField('Last Name/Surname', validators=[DataRequired(), Length(min=1, max=120)])
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=120)])
    email = EmailField('Email', validators=[DataRequired(), Length(min=5, max=120), Email()])
    nationality = SelectField('Nationality', choices=countries_data, validate_choice=True, validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    country = SelectField('Residential Country', validators=[DataRequired()], choices=countries_data, validate_choice=True)
    city = SelectField('City', validators=[DataRequired()])
    address = StringField('Address', validators=[Optional()])
    country_code = SelectField('Country Code', validators=[DataRequired()])
    phone_no = TelField('Phone Number', validators=[Optional(), Length(min=11, max=14)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=120)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo(fieldname=password, message='Password Must Match!')])
    submit = SubmitField('Submit')