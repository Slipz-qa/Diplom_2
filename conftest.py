import pytest
from tests.methods import UserActions
from data import BASE_URL, HEADERS
import requests


@pytest.fixture
def user_data():
    return {
        "email": UserActions.generate_unique_email(),
        "password": "testpass123",
        "name": "Test User"
    }

@pytest.fixture
def auth_token(user_data):
    UserActions.register_user(user_data)
    response = UserActions.login_user(user_data)
    response_json = response.json()
    return response_json["accessToken"]


@pytest.fixture
def authorized_headers(auth_token):
    return {**HEADERS, "Authorization": f"Bearer {auth_token}"}


@pytest.fixture
def ingredients():
    response = requests.get(f"{BASE_URL}/ingredients", headers=HEADERS)
    assert response.status_code == 200, "Failed to get ingredients"
    return [ingredient["_id"] for ingredient in response.json().get("data", [])]


@pytest.fixture
def create_test_user(user_data):
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data, headers=HEADERS)
    assert response.status_code == 200, "Failed to create test user"
    access_token = response.json().get("accessToken")

    yield user_data, access_token

    delete_response = requests.delete(f"{BASE_URL}/auth/user", headers={"Authorization": f"Bearer {access_token}"})
    if delete_response.status_code != 200:
        print(f"Failed to delete test user: {delete_response.status_code}, {delete_response.json()}")





















