from api.base_url import BaseUrl


class DeleteNotes(BaseUrl):
    """Удаление заметки через метод DELETE"""

    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def delete_notes(self, note_id, need_token=True, token=None):
        if token:
            self.token = token
        response = self._request(method="DELETE", note_id=note_id, need_token=need_token)
        return response
    