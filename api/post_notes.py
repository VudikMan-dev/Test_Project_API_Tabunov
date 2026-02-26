import requests

from api.post_authorization import PostAuthorization
from test.data.json_for_post_notes import JsonForPostNotesTest


class PostNotes:
    def __init__(self, token):
        self.token = token
    BASE_URL = "http://185.240.103.201:8000/api/notes"

    def headers_post_notes(self):
        return {"accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"}

    def creating_note(self):
        response = requests.post(url=self.BASE_URL,
                                 headers=self.headers_post_notes(),
                                 json=JsonForPostNotesTest.DATA_POST_NOTES)
        return response
