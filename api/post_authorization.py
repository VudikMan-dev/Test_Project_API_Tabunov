from api.base_url import BaseUrl


class PostAuthorization(BaseUrl):
    """Авторизация с помощью метода POST"""
    ENDPOINT = "/api/login"
    token = ""

    def user_authorization(self, email, password):
        """Метод для отправки запроса на авторизацию"""
        body = {"email": email, "password": password}
        response_authorization = self._request(method="POST", json=body)
        return response_authorization

    def get_token(self, email, password):
        """Метод для получения токена"""
        auth = self.user_authorization(email, password)
        return auth.json()["token"]
