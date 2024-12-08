import pytest
import allure
from methods import UserActions, ResponseValidator
from helpers import Helper

class TestCreateUser:

    @allure.title("Проверка наличия токена доступа при создании уникального пользователя")
    @allure.step("Регистрация уникального пользователя и проверка наличия токена доступа в ответе")
    def test_create_unique_user_token_present(self):
        user_data = {
            "email": Helper.generate_unique_email(),
            "password": "testpass123",
            "name": "Test User"
        }

        response = UserActions.register_user(user_data)

        # Проверка наличия токена в ответе
        assert "accessToken" in response, "Токен доступа не найден в ответе"

    @allure.title("Проверка успешного создания уникального пользователя")
    @allure.step("Регистрация уникального пользователя и проверка флага успеха в ответе")
    def test_create_unique_user_success(self):
        user_data = {
            "email": Helper.generate_unique_email(),
            "password": "testpass123",
            "name": "Test User"
        }

        response = UserActions.register_user(user_data)

        # Проверка успешного создания пользователя
        assert response.get("success") == True, f"Expected success: True, got {response.get('success')}"

    @allure.title("Проверка ошибки при создании уже существующего пользователя")
    @allure.step("Попытка регистрации существующего пользователя и проверка выбрасываемого исключения")
    def test_create_existing_user_raises_exception(self, create_test_user):
        user_data, _ = create_test_user
        with pytest.raises(ValueError) as exc_info:
            UserActions.register_user(user_data)

        # Проверка, что ошибка при попытке создать существующего пользователя
        assert "User already exists" in str(exc_info.value), "Сообщение об ошибке отличается"

    @allure.title("Проверка кодов статуса при создании пользователя с отсутствующими обязательными полями")
    @allure.step("Регистрация пользователя с отсутствующими обязательными полями и проверка кодов статуса")
    @pytest.mark.parametrize(
        "user_data, expected_status_code",
        [
            ({"email": Helper.generate_unique_email(), "name": "Test User"}, 403),
            ({"name": "Test User", "password": "testpass123"}, 403),
        ]
    )
    def test_create_user_missing_field_status_code(self, user_data, expected_status_code):
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/register",
            json=user_data
        )

        # Проверка статус кода
        ResponseValidator.check_status_code(response, expected_status_code)

    @allure.title("Проверка сообщений об ошибке при создании пользователя с отсутствующими обязательными полями")
    @allure.step("Регистрация пользователя с отсутствующими обязательными полями и проверка сообщения об ошибке")
    @pytest.mark.parametrize(
        "user_data, expected_message",
        [
            ({"email": Helper.generate_unique_email(), "name": "Test User"},
             "Email, password and name are required fields"),
            ({"name": "Test User", "password": "testpass123"}, "Email, password and name are required fields"),
        ]
    )
    def test_create_user_missing_field_message(self, user_data, expected_message):
        response = UserActions.make_request(
            method="POST",
            endpoint="/auth/register",
            json=user_data
        )

        # Проверка сообщения об ошибке
        assert response.json()["message"] == expected_message, f"Ожидалось сообщение: {expected_message}, получено: {response.json()['message']}"





























