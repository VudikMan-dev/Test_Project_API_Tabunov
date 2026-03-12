from api.base_url import BaseUrl


class DeleteNotes(BaseUrl):
    # Удаление заметки через метод DELETE с помощью id
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def delete_notes(self, note_id):
        responses = self._request(method="Delete", need_token=True)
        return responses
