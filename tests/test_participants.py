def test_remove_participant_successful(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # Known participant

    # Act
    response = client.delete(f"/activities/{activity}/participants/{email}")

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert "Removed" in result["message"]
    assert email in result["message"]

    # Verify removal persisted
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert email not in activities[activity]["participants"]


def test_remove_participant_activity_not_found(client):
    # Arrange
    nonexistent_activity = "Nonexistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{nonexistent_activity}/participants/{email}"
    )

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert "Activity not found" in result["detail"]


def test_remove_participant_not_found(client):
    # Arrange
    activity = "Chess Club"
    email = "notmember@mergington.edu"  # Not a participant

    # Act
    response = client.delete(f"/activities/{activity}/participants/{email}")

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert "Participant not found" in result["detail"]


def test_remove_participant_updates_list(client):
    # Arrange
    activity = "Programming Class"
    initial_response = client.get("/activities")
    initial_participants = initial_response.json()[activity]["participants"].copy()
    email_to_remove = initial_participants[0]  # Get first participant

    # Act
    client.delete(f"/activities/{activity}/participants/{email_to_remove}")
    updated_response = client.get("/activities")
    updated_participants = updated_response.json()[activity]["participants"]

    # Assert
    assert len(updated_participants) == len(initial_participants) - 1
    assert email_to_remove not in updated_participants
