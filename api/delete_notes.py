import requests
from api.base_url import BaseUrl
        # Удаление заметки через метод DELETE с помощью id


class DeleteNotes:
    URL = f"{BaseUrl.BASE_URL}/api/notes"
    def __init__(self, token):
        self.token = token

    def headers_delete_notes(self):
        return {"accept": "application/json",
                "Authorization": f"Bearer {self.token}"}

    def delete_notes(self, note_id):
        responses = requests.delete(url=f"{self.URL}/{note_id}", headers=self.headers_delete_notes())
        return responses
