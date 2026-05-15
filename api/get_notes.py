from api.base_url import BaseUrl


class GetNotes(BaseUrl):
    """Получение id заметки через метод GET"""
    ENDPOINT = "/api/notes"

    def __init__(self, token):  # Конструктор
        self.token = token

    def get_notes(self):
        """Метод получения всех заметок"""
        response = self._request(method="GET", need_token=True)
        return response

    def get_note_by_title(self, title):
        """Метод поиска заметки по заголовку"""
        response = self.get_notes()
        notes = response.json()  # получаем список заметок, превращаем ответ в JSON
        for note in notes:
            if title in note["title"]:
                return note["id"]  # Как только нашли совпадение — возвращаем ID заметки
        return None  # Если ни одна заметка не подошла — возвращаем None
