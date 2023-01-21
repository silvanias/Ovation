def test_landing(client):
    response = client.get("/")
    assert b"<h1>About Page</h1>" in response.data
