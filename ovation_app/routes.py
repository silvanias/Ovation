from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db
from werkzeug.security import generate_password_hash
routes = Blueprint('routes', __name__)

@routes.route('/')
def landing():
    return render_template('landing.html')

@routes.route('/login')
def login():
    return render_template('auth/login.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 5:
            flash('Passwords must be 5 or more characters', category='error')
        else:
            new_user = User(email = email, firstName = firstName, lastName = lastName, password = generate_password_hash(password1, method = 'pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User Created!', category='success')
            return redirect(url_for('routes.profile'))
            
            
    data = request.form
    print(data)
    return render_template('auth/signup.html')

@routes.route('/profile')
def profile():
    return render_template('profile.html')