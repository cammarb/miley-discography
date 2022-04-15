def test_index_success(client):
    # Page loads
    response = client.get("/songs")
    assert response.status_code == 200
    # The assert statement checks if the string 'this text does not exist' is part of the HTML code that is represented by response.data
    assert b"this text does not exist" in response.data
