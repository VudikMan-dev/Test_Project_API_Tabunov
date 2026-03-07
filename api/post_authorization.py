import requests

from test.data.json_for_post_autorization import JsonForPostAuthorization
from api.base_url import BaseUrl
        # Авторизация с помощью метода POST


class PostAuthorization:
    URL = f"{BaseUrl.BASE_URL}/api/login"
    HEADERS_AUTHORIZATION = {"accept": "application/json", "Content-Type": "application/json"}
    token = ""
    def get_token(self):
        response = requests.post(url=f"{self.URL}",
                      headers=self.HEADERS_AUTHORIZATION,
                      json=JsonForPostAuthorization.DATA_POST_AUTHORIZATION)
        self.token = response.json()["token"]
        return self.token
