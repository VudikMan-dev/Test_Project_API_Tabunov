class TestCreateApi:
    def test_create_note(self, post_notes, teardown_note_delete):
        response = post_notes.creating_note()
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["message"] == "Заметка создана!"
