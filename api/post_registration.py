import requests
from test.data.json_for_post_registration import JsonForPostRegistration
from api.base_url import BaseUrl
        # Регистрация с помощью метода POST


class PostRegistration:
    URL = f"{BaseUrl.BASE_URL}/api/register"
    HEADERS_REGISTRATION = {"accept": "application/json", "Content-Type": "application/json"}
    def user_registration(self):
        response_registration = requests.post(url=f"{self.URL}",
                                              headers=self.HEADERS_REGISTRATION,
                                              json=JsonForPostRegistration.DATA_POST_REGISTRATION)
        return response_registration
