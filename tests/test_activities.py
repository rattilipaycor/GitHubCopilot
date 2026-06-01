def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_activity_name = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert expected_activity_name in payload
    assert {"description", "schedule", "max_participants", "participants"}.issubset(
        payload[expected_activity_name].keys()
    )
    assert isinstance(payload[expected_activity_name]["participants"], list)
