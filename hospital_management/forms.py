from optparse import Option
from tokenize import String
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SelectField, EmailField, PasswordField, SubmitField, DateField, TelField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Optional, ValidationError
from hospital_management.utils import countries, age
from hospital_management.models import User

title = ['Mr', 'Miss', 'Mrs', 'Dr Mr', 'Dr Miss', 'Dr Mrs']
blood = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
geno = ['AA', 'AC', 'AS', 'CC', 'SC', 'SS']
country = countries()

class NonValidatingSelectField(SelectField):
    def pre_validate(self, form):
        pass

class RegisterForm(FlaskForm):
    title = SelectField('Title', choices=title, validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=120)])
    last_name = StringField('Surname', validators=[DataRequired(), Length(min=1, max=120)])
    other_name = StringField('Other Name', validators=[Optional(), Length(min=0, max=120)])
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=120)])
    email = EmailField('Email', validators=[DataRequired(), Length(min=5, max=120), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=120)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Password Must Match!')])
    nationality = NonValidatingSelectField('Nationality', choices=country, validators=[Optional()])
    country = NonValidatingSelectField('Residential Country', choices=country, validators=[Optional()], validate_choice=False)
    country_code = NonValidatingSelectField('Country Code', validators=[Optional()], validate_choice=False)
    city = StringField('City', validators=[DataRequired()])
    address = StringField('Address', validators=[Optional()])
    phone_no = TelField('Phone Number', validators=[Optional(), Length(min=10, max=14)])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email already exists')

    def validate_phone_no(self, phone_no):
        yphone_no = self.country_code.data + phone_no.data
        user = User.query.filter_by(phone_no=yphone_no).first()
        if user:
            print(yphone_no)
            raise ValidationError('This phone number already exists')

    def validate_date_of_birth(self, date_of_birth):
        yAge = age(date_of_birth.data)
        if yAge < 18:
            raise ValidationError('You must be greater than 18 years!')


class LoginForm(FlaskForm):
    username = StringField('Username or Email', validators=[DataRequired(), Length(min=6, max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=120)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class UpdateAccountForm(FlaskForm):
    title = SelectField('Title', choices=title, validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=120)])
    last_name = StringField('Surname', validators=[DataRequired(), Length(min=1, max=120)])
    other_name = StringField('Other Name', validators=[Optional(), Length(min=0, max=120)])
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=120)])
    email = EmailField('Email', validators=[DataRequired(), Length(min=5, max=120), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=120)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Password Must Match!')])
    nationality = NonValidatingSelectField('Nationality', choices=country, validators=[Optional()])
    country = NonValidatingSelectField('Residential Country', choices=country, validators=[Optional()], validate_choice=False)
    city = StringField('City', validators=[DataRequired()])
    address = StringField('Address', validators=[Optional()])
    phone_no = TelField('Phone Number', validators=[Optional(), Length(min=10, max=14)])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user != current_user:
            raise ValidationError('This username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user != current_user:
            raise ValidationError('This email already exists')

    def validate_phone_no(self, phone_no):
        user = User.query.filter_by(phone_no=phone_no.data).first()
        if user != current_user:
            raise ValidationError('This phone number already exists')

    def validate_date_of_birth(self, date_of_birth):
        yAge = age(date_of_birth.data)
        if yAge < 18:
            raise ValidationError('You must be greater than 18 years!')


class AddPatientsForm(FlaskForm):
    firstName = StringField('First Name of Patient', validators=[DataRequired(), Length(min=6, max=120)])
    lastName = StringField('Last Name of Patient', validators=[DataRequired(), Length(min=6, max=120)])
    otherName = StringField('Other Name of Patient', validators=[Optional(), Length(min=6, max=120)])
    patientAge = StringField('Age', validators=[DataRequired()])
    ailment = StringField('Ailment', validators=[DataRequired()])
    bloodGroup = NonValidatingSelectField('Blood Group', choices=blood, validators=[Optional()], validate_choice=False)
    genoType = NonValidatingSelectField('Genotype', choices=geno, validators=[Optional()], validate_choice=False)
    addressPatient = StringField('Address', validators=[DataRequired()])
    cityPatient = StringField('City', validators=[DataRequired()])
    statePatient = StringField('State', validators=[DataRequired()])
    countryPatient = NonValidatingSelectField('Country', choices=country, validators=[Optional()], validate_choice=False)
    phone_noPatient = TelField('Phone Number', validators=[Optional()])
    
    nameOfKin = StringField('Name of Next of Kin', validators=[DataRequired(), Length(min=5, max=200)])
    addressOfKin = StringField('Address of Next of Kin', validators=[DataRequired()])
    cityOfKin = StringField('City', validators=[DataRequired()])
    stateOfKin = StringField('State', validators=[DataRequired()])
    countryOfKin = SelectField('Country', choices=country, validators=[DataRequired()], validate_choice=False)
    phoneNoOfKin = TelField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Submit')