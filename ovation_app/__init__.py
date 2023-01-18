from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db = SQLAlchemy()
    
def create_app():
    db.init_app(app)

    from .routes import routes

    app.register_blueprint(routes, url_prefix = '/')

    from .models import User

    with app.app_context():
        db.create_all()

    return app


