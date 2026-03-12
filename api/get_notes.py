from api.base_url import BaseUrl


class GetNotes(BaseUrl):
    #  Получение id заметки через метод GET
    ENDPOINT = "/api/notes"

    def __init__(self, token):
        self.token = token

    def get_notes(self):
        response = self._request(method="GET", need_token=True)
        return response

    def get_note_by_title(self, title):
        response = self.get_notes()
        note = response.json() # получаем список заметок
        for note in note:
            if title in note["title"]:
                return note["id"]
        return None

token = BaseUrl.token
notes = GetNotes(token).get_notes().json()
print(notes)