class TestAuthorization:
    def test_user_authorization(self, post_authorization):
        """Проверка на статус код 200 (Успешная авторизация)"""
        response = post_authorization.user_authorization(email="stringhfvd4hv@mail.ru", password="1212121221")
        assert response.status_code == 200

    def test_user_authorization_wrong_password(self, post_authorization):
        """Проверка на статус код 401 (Ошибка авторизации)
        и текста "message": Ошибка авторизации... Пожалуйста, проверь почту или пароль"""
        response = post_authorization.user_authorization(email="stringhfvd4hv@mail.ru", password="wrong_password")
        assert response.status_code == 401
        assert response.json()["message"] == "Ошибка авторизации... Пожалуйста, проверь почту или пароль"
