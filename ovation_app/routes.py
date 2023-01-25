from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, login_manager


routes = Blueprint('routes', __name__)

@routes.route('/')
def landing():
    return render_template('landing.html')

@routes.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category = 'success')
                login_user(user, remember = True)
                login_manager.session['firstName'] = user.firstName
                return redirect(url_for('routes.profile'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')

    return render_template('auth/login.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('This email already exists, please login instead.', category = 'error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 5:
            flash('Passwords must be 5 or more characters', category='error')
        else:
            new_user = User(email = email, firstName = firstName, lastName = lastName, password = generate_password_hash(password1, method = 'pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User Created!', category='success')
            return redirect(url_for('routes.login'))
    
    data = request.form
    print(data)
    return render_template('auth/signup.html')

@routes.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))