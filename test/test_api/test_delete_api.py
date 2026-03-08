class TestDeleteApi:

    def test_delete_notes(self, delete_notes, setup_create_note_id):
        response = delete_notes.delete_notes(setup_create_note_id)
        assert response.status_code == 200
