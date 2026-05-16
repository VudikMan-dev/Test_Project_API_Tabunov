from api.get_notes import GetNotes


class TestGetNotesApi:
    def test_get_notes(self, notes_client, setup_teardown_note):
        """Проверка статус кода и что заметок больше нуля"""
        response = notes_client.get_notes()
        json_response = response.json()
        assert response.status_code == 200
        assert len(json_response) > 0

    def test_get_notes_without_token(self, notes_client):
        """Проверка статус кода 401 при отсутствии токена и ответа ("message": "Token is missing!")"""
        response = notes_client._request(method="GET", need_token=False)
        assert response.status_code == 401
        assert response.json()["message"] == "Token is missing!"

    def test_get_notes_invalid_token(self):
        """Проверека на невалидный токен, неверный или истек 403
        и текста ("message": "Token is invalid or expired!")"""
        invalid_token = "invalid_token_123"
        client = GetNotes(invalid_token)
        response = client.get_notes()
        assert response.status_code == 403
        assert response.json()["message"] == "Token is invalid or expired!"
