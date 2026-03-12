class TestRegistration:
    def test_user_registration(self, post_registration):
        response = post_registration.user_registration()
        assert response.status_code == 201
