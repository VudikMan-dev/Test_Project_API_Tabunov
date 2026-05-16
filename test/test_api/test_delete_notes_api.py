from api.delete_notes import DeleteNotes


class TestDeleteNotesApi:
    def test_delete_notes(self, delete_client, setup_create_note):
        """Проверка статус кода 200 и ответа Заметка создана!"""
        response = delete_client.delete_notes(setup_create_note)
        assert response.status_code == 200

    def test_delete_notes_without_token(self, delete_client, setup_create_note):
        """Проверка статус кода 401 и текста Token is missing!"""
        response = delete_client.delete_notes(setup_create_note, need_token=False)
        json_response = response.json()
        assert response.status_code == 401
        assert json_response["message"] == "Token is missing!"

    def test_delete_notes_invalid_token(self, delete_client, setup_create_note, teardown_note_delete):
        """Проверка статус кода 403 и текста Token is invalid or expired!"""
        response = delete_client.delete_notes(setup_create_note, token="invalid_token")
        json_response = response.json()
        assert response.status_code == 403
        assert json_response["message"] == "Token is invalid or expired!"

    def test_delete_other_user_note(self, second_user_token, setup_create_note, teardown_note_delete):
        another_delete_client = DeleteNotes(second_user_token)
        response = another_delete_client.delete_notes(setup_create_note)
        json_response = response.json()
        assert response.status_code == 409
        assert json_response["message"] == "Not authorized to delete this note!"
        # тут баг, по требовнаиям в конйе текста должен быть восклицательный знак
