import requests
from api.base_url import BaseUrl
        #  Получение id заметки через метод GET


class GetNotes:
    def __init__(self, token):
        self.token = token
    URL = f"{BaseUrl.BASE_URL}/api/notes"

    def get_headers(self):
        return {"accept": "application/json", "Authorization": f"Bearer {self.token}"}

    def get_notes(self):
        response = requests.get(url=f"{self.URL}", headers=self.get_headers())
        return response

    def get_note_by_title(self, title):
        response = self.get_notes()
        notes = response.json() # получаем список заметок
        for note in notes:
            if title in note["title"]:
                return note["id"]
        return None
