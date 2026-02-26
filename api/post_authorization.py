import requests

from test.data.json_for_post_autorization import JsonForPostAuthorization


class PostAuthorization:
    BASE_URL = "http://185.240.103.201:8000/api/login"
    HEADERS_AUTHORIZATION = {"accept": "application/json", "Content-Type": "application/json"}
    token = ""
    def get_token(self):
        response = requests.post(url=self.BASE_URL,
                      headers=self.HEADERS_AUTHORIZATION,
                      json=JsonForPostAuthorization.DATA_POST_AUTHORIZATION)
        self.token = response.json()["token"]
        return self.token

# a = PostAuthorization()
# print(a.get_token())
