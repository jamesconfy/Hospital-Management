from flask import current_app as app, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, logout_user, current_user, login_user
from datetime import timedelta
from hospital_management.forms import RegisterForm, LoginForm, UpdateAccountForm, AddPatientsForm
from hospital_management import bcrypt
from hospital_management import db
from hospital_management.models import User, Patient


@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        page = request.args.get('page', 1, type=int)
        patients = Patient.query.order_by(Patient.date_created.desc()).paginate(per_page=3, page=page)
        return render_template('index.html', title='Dashboard', patients=patients, legend='Home')
    else:
        return render_template('home.html', title='Dashboard')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(
                form.password.data).decode('utf-8')
            if form.other_name.data is None:
                form.other_name.data = ""
            if form.phone_no.data is not None:
                form.phone_no.data = form.country_code.data + form.phone_no.data

            user = User(title=form.title.data,
                        username=form.username.data,
                        email=form.email.data,
                        password=hashed_password,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        other_name=form.other_name.data,
                        nationality=form.nationality.data,
                        country=form.country.data,
                        city=form.city.data,
                        address=form.address.data,
                        country_code=form.country_code.data,
                        phone_no=form.phone_no.data,
                        date_of_birth=form.date_of_birth.data)

            db.session.add(user)
            db.session.commit()
            flash(
                f'Account created successfully for {form.username.data}', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', form=form, title='Register')


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=2)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()

            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)

                next_url = request.form.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect(url_for('home'))
            else:
                flash('Login Unsuccesful, check username or password', 'danger')
    return render_template('login.html', form=form, title='Login')


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.other_name.data = current_user.other_name
        form.nationality.data = current_user.nationality
        form.country.data = current_user.country
 #       form.country_code.data = current_user.country_code
        form.phone_no.data = current_user.phone_no
        form.city.data = current_user.city
        form.address.data = current_user.address
        form.title.data = current_user.title
        form.date_of_birth.data = current_user.date_of_birth

    elif request.method == 'POST':
        if form.validate_on_submit():
            current_user.username = form.username.data
            current_user.email = form.email.data
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.other_name = form.other_name.data
            current_user.nationality = form.nationality.data
            current_user.country = form.country.data
#            current_user.country_code = form.country_code.data
            current_user.phone_no = form.phone_no.data
            current_user.city = form.city.data
            current_user.address = form.address.data
            current_user.title = form.title.data
            current_user.date_of_birth = form.date_of_birth.data

    return render_template('account.html', form=form)

@app.route('/doctors')
def doctors():
    page = request.args.get('page', 1, type=int)
    doctors = User.query.order_by(User.date_created.desc()).paginate(per_page=3, page=page)
    return render_template('doctors.html', title='Doctors', doctors=doctors, legend='List of Doctors')

@app.route('/doctors/<string:name>###<int:doctor_id>###')
def doctor(name, doctor_id):
    doctor = User.query.filter_by(id=doctor_id).first()
    title = f"Profile of {doctor.first_name} {doctor.other_name} {doctor.last_name}"
    legend = f"{doctor.first_name} {doctor.other_name} {doctor.last_name}"
    return render_template('doctor.html', title=title, legend=legend, doctor=doctor)

@app.route('/patient', methods=['GET', 'POST'])
@login_required
def patient():
    form = AddPatientsForm()
    if request.method == 'POST':
        patient = Patient(firstName=form.firstName.data,
                          lastName=form.lastName.data,
                          otherName=form.otherName.data,
                          patientAge=form.patientAge.data,
                          ailment=form.ailment.data,
                          stateOfMind=form.stateOfMind.data,
                          bloodGroup=form.bloodGroup.data,
                          genoType=form.genoType.data,
                          addressPatient=form.addressPatient.data,
                          cityPatient=form.cityPatient.data,
                          statePatient=form.statePatient.data,
                          countryPatient=form.countryPatient.data,
                          phone_noPatient=form.phone_noPatient.data,

                          nameOfKin=form.nameOfKin.data,
                          addressOfKin=form.addressOfKin.data,
                          cityOfKin=form.cityOfKin.data,
                          stateOfKin=form.stateOfKin.data,
                          countryOfKin=form.countryOfKin.data,
                          phoneNoOfKin=form.phoneNoOfKin.data,
                          doctor=current_user)
        db.session.add(patient)
        db.session.commit()
        flash(
            f'You have another patient added to your list, {form.firstName.data} {form.lastName.data} {form.otherName.data if form.otherName.data is not None else ""}', 'success')
        return redirect(url_for('home'))

    return render_template('patient.html', title='Add Patients', form=form)    

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logout successfully', 'success')
    return redirect(url_for('home'))
