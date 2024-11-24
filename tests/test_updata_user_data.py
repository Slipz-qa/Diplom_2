from tests.methods import UserActions

class TestUserUpdate:

    def test_update_user_with_auth_status_code_name(self, create_test_user):
        _, auth_token = create_test_user
        update_data = {"name": "New Name"}

        response = UserActions.update_user_data(auth_token, update_data)

        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


    def test_update_user_with_auth_name(self, create_test_user):
        _, auth_token = create_test_user
        update_data = {"name": "New Name"}


        response = UserActions.update_user_data(auth_token, update_data)

        assert response.json()["user"]["name"] == "New Name", "User name was not updated correctly"


    def test_update_user_with_auth_email(self, create_test_user):
        _, auth_token = create_test_user
        new_email = UserActions.generate_unique_email()
        update_data = {"email": new_email}


        response = UserActions.update_user_data(auth_token, update_data)

        if response.status_code == 200:
            assert response.json().get("user", {}).get("email") == new_email, "User email was not updated correctly"
        else:
            assert response.json().get("message") == "User with such email already exists", "Unexpected error message"


    def test_update_user_with_auth_password(self, create_test_user):
        _, auth_token = create_test_user
        new_password = "newpassword123"
        update_data = {"password": new_password}

        response = UserActions.update_user_data(auth_token, update_data)

        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


    def test_update_user_with_new_password_login(self, create_test_user):
        _, auth_token = create_test_user
        new_password = "newpassword123"
        update_data = {"password": new_password}

        response = UserActions.update_user_data(auth_token, update_data)


        new_email = response.json()["user"]["email"]
        login_data = {"email": new_email, "password": new_password}
        login_response = UserActions.login_user(login_data)

        assert login_response.status_code == 200, f"Expected status code 200, but got {login_response.status_code}"


    def test_update_user_without_auth_name_status_code(self):
        update_data = {"name": "New Name"}

        response = UserActions.make_request("PATCH", "/auth/user", json=update_data)

        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"


    def test_update_user_without_auth_name_error_message(self):
        update_data = {"name": "New Name"}

        response = UserActions.make_request("PATCH", "/auth/user", json=update_data)

        assert response.json()["message"] == "You should be authorised", "Error message is incorrect"


    def test_update_user_without_auth_email_status_code(self):
        update_data = {"email": "new_email@example.com"}

        response = UserActions.make_request("PATCH", "/auth/user", json=update_data)

        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"


    def test_update_user_without_auth_email_error_message(self):
        update_data = {"email": "new_email@example.com"}

        response = UserActions.make_request("PATCH", "/auth/user", json=update_data)

        assert response.json()["message"] == "You should be authorised", "Error message is incorrect"

    def test_update_user_without_auth_password_status_code(self):
        update_data = {"password": "newpassword123"}

        response = UserActions.make_request("PATCH", "/auth/user", json=update_data)

        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"


    def test_update_user_without_auth_password_error_message(self):
        update_data = {"password": "newpassword123"}

        response = UserActions.make_request("PATCH", "/auth/user", json=update_data)

        assert response.json()["message"] == "You should be authorised", "Error message is incorrect"













