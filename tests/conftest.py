import pytest

from ovation_app import create_app, db 

@pytest.fixture()
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

    with app.app_context():
        db.create_all()
    
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
