from tests.methods import UserActions

class TestUserLogin:

    def test_login_existing_user_status_code(self, create_test_user):
        user_data, _ = create_test_user
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/login",
            json=user_data
        )
        assert response.status_code == 200, "Код ответа должен быть 200 при успешном логине"

    def test_login_existing_user_contains_access_token(self, create_test_user):
        user_data, _ = create_test_user
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/login",
            json=user_data
        )
        assert "accessToken" in response.json(), "Токен доступа должен присутствовать в ответе"


    def test_login_existing_user_success_flag(self, create_test_user):
        user_data, _ = create_test_user
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/login",
            json=user_data
        )
        assert response.json().get("success") is True, "Поле 'success' должно быть True при успешном логине"


    def test_login_invalid_credentials_status_code(self):
        user_data = {
            "email": "invalid_user@example.com",
            "password": "wrongpassword"
        }
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/login",
            json=user_data
        )
        assert response.status_code == 401, "Код ответа должен быть 401 при неверных данных"


    def test_login_invalid_credentials_error_message(self):
        user_data = {
            "email": "invalid_user@example.com",
            "password": "wrongpassword"
        }
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/login",
            json=user_data
        )
        error_message = response.json().get("message")
        assert error_message == "email or password are incorrect", "Сообщение об ошибке должно быть корректным"


