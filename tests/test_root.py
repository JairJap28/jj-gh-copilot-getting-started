def test_root_redirects_to_index(client):
    # Arrange
    # No setup needed

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_root_follow_redirect(client):
    # Arrange
    # No setup needed

    # Act
    response = client.get("/", follow_redirects=True)

    # Assert
    assert response.status_code == 200
