from flask import current_app as app, render_template
from hospital_management.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home():
    return render_template("layout.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    return render_template('register.html', form=form)

