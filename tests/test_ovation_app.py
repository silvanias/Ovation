from ovation_app.models import User

def test_landing(client):
    response = client.get("/")
    assert b"<h1>About Page</h1>" in response.data



def test_signup(client, app):
    response = client.post("/signup", data={"email": "test@test.com", "firstName": "Silas", "lastName":"Meow" ,"password":"test" ,"confirmPassword":"passwordTest"})

    with app.app_contect():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"
        assert User.query.first().firstName == "Silas"
        assert User.query.first().lastName == "Meow"
        assert User.query.first().password == "passwordTest"