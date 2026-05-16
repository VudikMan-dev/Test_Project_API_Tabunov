from api.base_url import BaseUrl


class PostNotes(BaseUrl):
    """Создание заметки через метод POST"""

    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def create_note(self, body, need_token=True, token=None):
        if token:
            self.token = token
        response = self._request(method="POST", need_token=need_token, json=body)
        return response
