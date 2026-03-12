from test.data.json_for_post_notes import JsonForPostNotesTest
from api.base_url import BaseUrl


class PostNotes(BaseUrl):
    # Создание заметки через метод POST
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def create_note(self):
        response = self._request(method="Post", need_token=True,
                                 json=JsonForPostNotesTest.DATA_POST_NOTES)
        return response

a = PostNotes(BaseUrl)
print(a.create_note())