from ovation_app.models import User
from sqlalchemy.sql import func

def test_landing(client):
    response = client.get("/")
    assert b"<h1>About Page</h1>" in response.data

"""  NOT WORKING AT THE MOMENT
def test_signup(client, app):
    response = client.post("/signup", 
              data={"email": "test@test.com", 
                "firstName": "Silas",
                "lastName":"Meow" ,
                "password1":"test" , 
                "password2":"passwordTest", 
                "creationDate":func.now()})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"
        assert User.query.first().firstName == "Silas"
        assert User.query.first().lastName == "Meow"
        assert User.query.first().password == "passwordTest"
"""