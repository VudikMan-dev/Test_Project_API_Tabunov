from test.data.json_for_post_registration import JsonForPostRegistration
from api.base_url import BaseUrl


class PostRegistration(BaseUrl):  # Наследуемся от BaseUrl
    """Регистрация с помощью метода POST"""
    ENDPOINT = "/api/register"  # переопределяю endpoint для конкретной апишки

    def user_registration(self, data=None):
        if data is None:
            data = JsonForPostRegistration.DATA_POST_REGISTRATION
        return self._request(method="POST", json=data)
