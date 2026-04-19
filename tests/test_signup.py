def test_signup_successful(client):
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert email in result["message"]
    assert activity in result["message"]

    # Verify signup persisted
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert email in activities[activity]["participants"]


def test_signup_activity_not_found(client):
    # Arrange
    email = "student@mergington.edu"
    nonexistent_activity = "Nonexistent Activity"

    # Act
    response = client.post(
        f"/activities/{nonexistent_activity}/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert "Activity not found" in result["detail"]


def test_signup_duplicate_student_error(client):
    # Arrange
    # michael@mergington.edu is already in Chess Club
    email = "michael@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    result = response.json()
    assert "already signed up" in result["detail"].lower()


def test_signup_email_validation(client):
    # Arrange
    activity = "Programming Class"

    # Act
    response = client.post(
        f"/activities/{activity}/signup", params={"email": "alice@mergington.edu"}
    )
    activities_response = client.get("/activities")
    activities = activities_response.json()

    # Assert
    assert response.status_code == 200
    assert "alice@mergington.edu" in activities[activity]["participants"]
