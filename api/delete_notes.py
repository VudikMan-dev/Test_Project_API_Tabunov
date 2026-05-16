from api.base_url import BaseUrl


class DeleteNotes(BaseUrl):
    """Удаление заметки через метод DELETE с помощью id"""

    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def delete_notes(self, note_id):
        response = self._request(method="DELETE", note_id=note_id, need_token=True)
        return response

    def delete_notes_without_token(self, note_id):
        response = self._request(method="DELETE", note_id=note_id, need_token=False)
        return response

    def delete_notes_invalid_token(self, note_id):
        self.token = "invalid_token"
        response = self._request(method="DELETE", note_id=note_id, need_token=True)
        return response
