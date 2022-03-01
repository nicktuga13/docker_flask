def test_request_index(client):
    response = client.get("/")
    assert response.status.code == 200
    assert b"Index Page" in response.data


def test_request_about(client):
    response = client.get("/about")
    assert response.status.code == 200
    assert b"About Page" in response.data


def test_request_page1(client):
    response = client.get("/page1")
    assert response.status.code == 200
    assert b"Page 1" in response.data


def test_request_page2(client):
    response = client.get("/page2")
    assert response.status.code == 200
    assert b"Page 2" in response.data

