import requests  # Библиотека для отправки HTTP-запросов


class BaseUrl:  # Это базовый класс для работы с API.
    BASE_URL = "http://185.240.103.201:8000"  # Переменные класса
    token = ""
    ENDPOINT = ""

    def headers(self, need_token: bool):  # Метод в (скобках аргументы)
        if need_token:
            return {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"  # если есть токен поставь его
            }
        else:
            return {"Accept": "application/json",
                    "Content-Type": "application/json"}  # в противном случае не ставь его

    def _request(self, method: str, note_id: str = None, need_token=False, json=None):
        if note_id:
            url = f"{self.BASE_URL}{self.ENDPOINT}/{note_id}"  # если есть айди заметки добавляет его к URL
        else:
            url = f"{self.BASE_URL}{self.ENDPOINT}"  # если его нет то просто эндпоинт
        response = requests.request(method, url, headers=self.headers(need_token), json=json)
        return response
