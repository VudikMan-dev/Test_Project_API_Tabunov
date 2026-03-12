class TestAuthorization:
    def test_user_authorization(self, post_authorization):
        response = post_authorization.user_authorization()
        response_json = post_authorization.get_token()
        assert response.status_code == 200 # проверка на статус код
        assert len(response_json) > 0 # проверка на наличие токена

    # def test_user_authorization_wrong_password(self, post_authorization):
    #     response = post_authorization.user_authorization(password="wrong_password")
    #     print(response.json())
    #     assert response.status_code == 401
