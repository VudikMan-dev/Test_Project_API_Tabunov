import requests

class GetNotes:
    def __init__(self, token):
        self.token = token
    BASE_URL = "http://185.240.103.201:8000/api/notes"

    def get_headers(self):
        return {"accept": "application/json", "Authorization": f"Bearer {self.token}"}

    def get_notes(self):
        response = requests.get(url=self.BASE_URL, headers=self.get_headers())
        return response

    def get_note_by_title(self, title):
        response = self.get_notes()
        notes = response.json() # получаем список заметок
        for note in notes:
            if title in note["title"]:
                return note["id"]
        return None
