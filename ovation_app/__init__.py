from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder='templates')
    from .routes import routes

    app.register_blueprint(routes, url_prefix = '/')

    return app

