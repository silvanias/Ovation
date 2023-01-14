from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
    
def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    from .routes import routes

    app.register_blueprint(routes, url_prefix = '/')

    from .models import User

    with app.app_context():
        db.create_all()

    return app

