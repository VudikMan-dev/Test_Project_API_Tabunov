import requests


class DeleteNotes:
    BASE_URL = "http://185.240.103.201:8000/api/notes"
    def __init__(self, token):
        self.token = token

    def headers_delete_notes(self):
        return {"accept": "application/json", "Authorization": f"Bearer {self.token}"}

    def delete_notes(self, note_id):
        url = f"{self.BASE_URL}/{note_id}"
        responses = requests.delete(url=url, headers=self.headers_delete_notes())
        return responses
