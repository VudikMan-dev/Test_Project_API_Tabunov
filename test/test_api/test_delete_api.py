class TestDeleteApi:

    def test_delete_notes(self, delete_notes, setup_create_note):
        response = delete_notes.delete_notes(setup_create_note)
        assert response.status_code == 200
