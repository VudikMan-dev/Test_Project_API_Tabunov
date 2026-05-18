import random


class TestRegistration:
    def test_user_registration(self, post_registration):
        """Проверка на статус код 201"""
        valid_user = {
            "email": f"Tabunov{random.randint(1, 100000)}@mail.ru",
            "password": "123456",
            "username": f"Vadim{random.randint(1, 100000)}", }
        response = post_registration.user_registration(data=valid_user)
        assert response.status_code == 201

    def test_user_registration_message(self, post_registration):
        """Проверка сообщения при успешной регистрации"""
        valid_user = {
            "email": f"Tabunov{random.randint(1, 100000)}@mail.ru",
            "password": "123456",
            "username": f"Vadim{random.randint(1, 100000)}", }
        response = post_registration.user_registration(data=valid_user)
        assert response.json()["message"] == "Успешная регистрация!"

    def test_user_registration_bad_request(self, post_registration):
        """Проверка статус кода при неправильном запросе"""
        response = post_registration.user_registration(data={})
        assert response.status_code == 400, f"Ожидали 400, получили {response.status_code}"

    def test_registration_duplicate_email(self, post_registration):
        """проверка Пользователь с таким email уже существует 409"""
        user = {
            "email": f"test{random.randint(1, 100000)}@mail.ru",
            "password": "123456",
            "username": f"user{random.randint(1, 100000)}"}
        # первая регистрация
        response1 = post_registration.user_registration(data=user)
        assert response1.status_code == 201
        # вторая регистрация с тем же email
        response2 = post_registration.user_registration(data=user)
        assert response2.status_code == 409
        # проверка message
        assert response2.json()["message"] == "Пользователь с таким email уже существует"
