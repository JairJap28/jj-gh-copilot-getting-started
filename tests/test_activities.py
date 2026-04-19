def test_get_activities_returns_all_activities(client):
    # Arrange
    # No setup needed - activities are predefined in app.py

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert len(activities) > 0
    assert "Chess Club" in activities


def test_get_activities_has_required_fields(client):
    # Arrange
    # No setup needed

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for activity_name, activity_data in activities.items():
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)


def test_get_activities_participant_count_accuracy(client):
    # Arrange
    # Chess Club should have 2 participants by default

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert len(activities["Chess Club"]["participants"]) == 2
    assert "michael@mergington.edu" in activities["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in activities["Chess Club"]["participants"]
