import requests
from conftest import BASE_URL, HEADERS
from methods import  ResponseValidator

class TestGetUserOrders:

    def test_get_orders_authorized_user_status_code(self, auth_token):
        headers = {**HEADERS, "Authorization": auth_token}
        response = requests.get(f"{BASE_URL}/orders", headers=headers)
        ResponseValidator.check_status_code(response, 200)

    def test_get_orders_authorized_user_key_in_response(self, auth_token):
        headers = {**HEADERS, "Authorization": auth_token}
        response = requests.get(f"{BASE_URL}/orders", headers=headers)
        ResponseValidator.check_key_in_response(response, "orders")

    # Получение заказов неавторизованного пользователя
    def test_get_orders_unauthorized_user_status_code(self):
        response = requests.get(f"{BASE_URL}/orders", headers=HEADERS)
        ResponseValidator.check_status_code(response, 401)

    def test_get_orders_unauthorized_user_message(self):
        response = requests.get(f"{BASE_URL}/orders", headers=HEADERS)
        ResponseValidator.check_message_in_response(response, "You should be authorised")





