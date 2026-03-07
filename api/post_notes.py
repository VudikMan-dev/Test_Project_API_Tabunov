import requests
from test.data.json_for_post_notes import JsonForPostNotesTest
from api.base_url import BaseUrl
        # Создание заметки через метод POST


class PostNotes:
    def __init__(self, token):
        self.token = token
    URL = f"{BaseUrl.BASE_URL}/api/notes"

    def headers_post_notes(self):
        return {"accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"}

    def create_note(self):
        response = requests.post(url=f"{self.URL}",
                                 headers=self.headers_post_notes(),
                                 json=JsonForPostNotesTest.DATA_POST_NOTES)
        return response
