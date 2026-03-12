from test.data.json_for_post_autorization import JsonForPostAuthorization
from api.base_url import BaseUrl


class PostAuthorization(BaseUrl):
    """Авторизация с помощью метода POST"""
    ENDPOINT = "/api/login"
    token = ""

    def user_authorization(self, email=None, password=None):
        response_authorization = self._request(method="Post",
                                               json=JsonForPostAuthorization.DATA_POST_AUTHORIZATION)
        return response_authorization

    def get_token(self):
        auth = self.user_authorization()
        return auth.json()["token"]
