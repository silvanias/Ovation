from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from . import db
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
            #TODO flash 'Passwords must match'
            pass
        else:
            #TODO hash password
            new_user = User(email = email, firstName = firstName, lastName = lastName, password = password1)
            db.session.add(new_user)
            db.session.commit()
            #TODO flash 'Account created'
            return redirect(url_for('routes.landing'))
            
    data = request.form
    print(data)
    return render_template('auth/signup.html')

@routes.route('/profile')
def profile():
    return render_template('profile.html')