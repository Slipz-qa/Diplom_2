import pytest
from tests.methods import UserActions, ResponseValidator


class TestCreateUser:

    def test_create_unique_user_token_present(self):
        user_data = {
            "email": UserActions.generate_unique_email(),
            "password": "testpass123",
            "name": "Test User"
        }

        response = UserActions.register_user(user_data)
        assert "accessToken" in response, "Токен доступа не найден в ответе"

    def test_create_unique_user_success(self):
        user_data = {"email": UserActions.generate_unique_email(), "password": "testpass123", "name": "Test User"}

        response = UserActions.register_user(user_data)

        assert response.get("success") == True, f"Expected success: True, got {response.get('success')}"

    def test_create_existing_user_raises_exception(self, create_test_user):
        user_data, _ = create_test_user
        with pytest.raises(ValueError) as exc_info:
            UserActions.register_user(user_data)
        assert "User already exists" in str(exc_info.value), "Сообщение об ошибке отличается"

    @pytest.mark.parametrize(
        "user_data, expected_status_code",
        [
            ({"email": UserActions.generate_unique_email(), "name": "Test User"}, 403),
            ({"name": "Test User", "password": "testpass123"}, 403),
        ]
    )
    def test_create_user_missing_field_status_code(self, user_data, expected_status_code):
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/register",
            json=user_data
        )
        ResponseValidator.check_status_code(response, expected_status_code)

    @pytest.mark.parametrize(
        "user_data, expected_message",
        [
            ({"email": UserActions.generate_unique_email(), "name": "Test User"}, "Email, password and name are required fields"),
            ({"name": "Test User", "password": "testpass123"}, "Email, password and name are required fields"),
        ]
    )
    def test_create_user_missing_field_message(self, user_data, expected_message):
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/register",
            json=user_data
        )
        assert response.json()["message"] == expected_message, f"Ожидалось сообщение: {expected_message}, получено: {response.json()['message']}"



























