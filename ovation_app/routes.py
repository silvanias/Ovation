from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def landing():
    return render_template('landing.html')

@routes.route('/login')
def login():
    return render_template('auth/login.html')

@routes.route('/signup')
def signUp():
    return render_template('auth/signup.html')

@routes.route('/profile')
def profile():
    return render_template('profile.html')