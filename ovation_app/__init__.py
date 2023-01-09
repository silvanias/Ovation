from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
@app.route('/landing')
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

def create_app():
    return app