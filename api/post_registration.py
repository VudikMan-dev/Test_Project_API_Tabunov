import requests

from test.data.json_for_post_registration import JsonForPostRegistration


class PostRegistration:
    BASE_URL = "http://185.240.103.201:8000/api/register"
    HEADERS_REGISTRATION = {"accept": "application/json", "Content-Type": "application/json"}
    def user_registration(self):
        response_registration = requests.post(url=self.BASE_URL,
                                              headers=self.HEADERS_REGISTRATION,
                                              json=JsonForPostRegistration.DATA_POST_REGISTRATION)
        return response_registration
