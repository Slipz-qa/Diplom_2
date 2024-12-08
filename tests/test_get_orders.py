import requests
import allure
from conftest import BASE_URL, HEADERS
from methods import ResponseValidator


class TestGetUserOrders:

    @allure.title("Проверка статус-кода при получении заказов авторизованным пользователем")
    @allure.step("Отправка запроса на получение заказов авторизованным пользователем и проверка статус-кода")
    def test_get_orders_authorized_user_status_code(self, auth_token):
        headers = {**HEADERS, "Authorization": auth_token}
        response = requests.get(f"{BASE_URL}/orders", headers=headers)

        # Проверка статус кода
        ResponseValidator.check_status_code(response, 200)

        # Дополнительная проверка содержимого ответа
        response_json = response.json()
        assert isinstance(response_json, dict), "Response is not a valid JSON object"

    @allure.title("Проверка наличия ключа 'orders' в ответе для авторизованного пользователя")
    @allure.step("Отправка запроса на получение заказов авторизованным пользователем и проверка наличия ключа 'orders' в ответе")
    def test_get_orders_authorized_user_key_in_response(self, auth_token):
        headers = {**HEADERS, "Authorization": auth_token}
        response = requests.get(f"{BASE_URL}/orders", headers=headers)

        # Проверка наличия ключа "orders" в ответе
        ResponseValidator.check_key_in_response(response, "orders")

        # Дополнительная проверка, чтобы убедиться, что orders — это список
        response_json = response.json()
        assert isinstance(response_json["orders"], list), "'orders' is not a list"

    @allure.title("Проверка статус-кода при получении заказов неавторизованным пользователем")
    @allure.step("Отправка запроса на получение заказов неавторизованным пользователем и проверка статус-кода")
    def test_get_orders_unauthorized_user_status_code(self):
        response = requests.get(f"{BASE_URL}/orders", headers=HEADERS)

        # Проверка статус кода
        ResponseValidator.check_status_code(response, 401)

        # Проверка сообщения об ошибке
        response_json = response.json()
        assert response_json.get("message") == "You should be authorised", "Error message is incorrect"

    @allure.title("Проверка сообщения об ошибке при попытке получения заказов неавторизованным пользователем")
    @allure.step("Отправка запроса на получение заказов неавторизованным пользователем и проверка сообщения об ошибке")
    def test_get_orders_unauthorized_user_message(self):
        response = requests.get(f"{BASE_URL}/orders", headers=HEADERS)

        # Проверка сообщения об ошибке
        response_json = response.json()
        assert response_json.get("message") == "You should be authorised", "Error message is incorrect"






