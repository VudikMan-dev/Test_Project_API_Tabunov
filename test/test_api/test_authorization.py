from test.data.json_for_post_autorization import DATA_POST_AUTHORIZATION

class TestAuthorization:
    def test_user_authorization(self, post_authorization):
        """Проверка на статус код 200 (Успешная авторизация)"""
        response = post_authorization.user_authorization(email=DATA_POST_AUTHORIZATION["email"],
                                                         password=DATA_POST_AUTHORIZATION["password"])
        assert response.status_code == 200

    def test_user_authorization_wrong_password(self, post_authorization):
        """Проверка на статус код 401 (Ошибка авторизации)
        и текста "message": Ошибка авторизации... Пожалуйста, проверь почту или пароль"""
        response = post_authorization.user_authorization(email=DATA_POST_AUTHORIZATION["email"],
                                                         password="wrong_password")
        assert response.status_code == 401
        assert response.json()["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль"
