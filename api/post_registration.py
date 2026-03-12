from test.data.json_for_post_registration import JsonForPostRegistration
from api.base_url import BaseUrl


class PostRegistration(BaseUrl):
    """Регистрация с помощью метода POST"""
    ENDPOINT = "/api/register"

    def user_registration(self):
        response_registration = self._request(method=f"Post",
                                              json=JsonForPostRegistration.DATA_POST_REGISTRATION)
        return response_registration
