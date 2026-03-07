class TestGetApi:
    def test_get_notes(self, get_notes, setup_teardown_note):
        response = get_notes.get_notes()
        json_response = response.json()
        assert response.status_code == 200
