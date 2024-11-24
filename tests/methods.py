import requests
import random
import string
from data import BASE_URL, HEADERS

class UserActions:
    @staticmethod
    def generate_unique_email():

        return f"test_{''.join(random.choices(string.ascii_lowercase, k=8))}@example.com"

    @staticmethod
    def register_user(user_data):

        response = requests.post(f"{BASE_URL}/auth/register", json=user_data, headers=HEADERS)
        if response.status_code != 200:
            error_message = response.json().get("message", "Unknown error")
            raise ValueError(f"Failed to register user: {response.status_code}, {error_message}")
        return response.json()

    @staticmethod
    def make_request(method, endpoint, **kwargs):

        url = f"{BASE_URL}{endpoint}"
        headers = kwargs.pop("headers", HEADERS)
        response = requests.request(method, url, headers=headers, **kwargs)
        return response

    @staticmethod
    def update_user_data(auth_token, update_data):

        headers = {**HEADERS, "Authorization": auth_token}
        response = requests.patch(f"{BASE_URL}/auth/user", json=update_data, headers=headers)
        return response

    @staticmethod
    def login_user(login_data):

        response = requests.post(f"{BASE_URL}/auth/login", json=login_data, headers=HEADERS)
        if response.status_code != 200:
            raise ValueError(
                f"Failed to log in: {response.status_code}, {response.json().get('message', 'Unknown error')}")
        return response

    @staticmethod
    def send_create_order_request(order_data, auth_token=None):

        headers = {**HEADERS}
        if auth_token:
            headers["Authorization"] = auth_token

        response = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)
        return response


class ResponseValidator:
    @staticmethod
    def check_status_code(response, expected_code, expected_message=None):

        if isinstance(response, requests.Response):
            actual_status_code = response.status_code
        elif isinstance(response, dict):

            actual_status_code = 200 if response.get('success') else 400  # Пример: если success = True, код 200
        else:
            raise TypeError(f"Unsupported response type: {type(response)}")

        assert actual_status_code == expected_code, \
            f"Expected status {expected_code}, but got {actual_status_code}"

        if expected_message:
            actual_message = response.get('message', '')
            assert actual_message == expected_message, \
                f"Expected message: {expected_message}, but got {actual_message}"

    @staticmethod
    def check_key_in_response(response, key):
        assert key in response.json(), f"Response does not contain key: {key}"

    @staticmethod
    def check_message_in_response(response, expected_message):
        assert response.json()["message"] == expected_message, f"Expected message '{expected_message}', but got {response.json()['message']}"




