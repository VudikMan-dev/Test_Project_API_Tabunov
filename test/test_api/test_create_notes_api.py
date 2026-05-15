class TestCreateNotesApi:
    def test_create_note(self, post_notes, teardown_note_delete):
        """Проверка статус кода 201 и ответа Заметка создана!"""
        response = post_notes.create_note()
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["message"] == "Заметка создана!"

    def test_create_note_not_token(self, post_notes):
        """Проверка статус кода 401 и текста Token is missing!"""
        response = post_notes.create_note_without_token()
        json_response = response.json()
        assert response.status_code == 401
        assert json_response["message"] == "Token is missing!"

    def test_create_note_invalid_token(self, post_notes):
        """Проверка статус кода 403 и текста Token is invalid or expired!"""
        response = post_notes.create_note_invalid_token()
        json_response = response.json()
        assert response.status_code == 403
        assert json_response["message"] == "Token is invalid or expired!"
