# class BaseUrl:
#     BASE_URL = "http://185.240.103.201:8000"
import requests


class BaseUrl:
    BASE_URL = "http://185.240.103.201:8000"
    token = ""
    ENDPOINT = ""

    def headers (self, need_token: bool):
        if need_token:
            return {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }
        else:
            return {"Accept": "application/json",
                    "Content-Type": "application/json"}

    def _request(self, method: str, note_id: str = None, need_token=False, json=None):
        if note_id:
            url = f"{self.BASE_URL}{self.ENDPOINT}/{note_id}"
        else:
            url = f"{self.BASE_URL}{self.ENDPOINT}"
        response = requests.request(method, url, headers=self.headers(need_token), json=json)
        return response
