from methods import UserActions

class TestCreateOrder:

    def test_create_order_with_auth_status_code(self, auth_token, ingredients):
        order_data = {"ingredients": ingredients}
        response = UserActions.send_create_order_request(order_data, auth_token)
        assert response.status_code == 200

    def test_create_order_with_auth_order_key(self, auth_token, ingredients):
        order_data = {"ingredients": ingredients}
        response = UserActions.send_create_order_request(order_data, auth_token)
        response_json = response.json()
        assert "order" in response_json

    def test_create_order_without_auth_status_code(self, ingredients):
        order_data = {"ingredients": ingredients}
        response = UserActions.send_create_order_request(order_data)
        assert response.status_code == 200

    def test_create_order_without_auth_order_key(self, ingredients):
        order_data = {"ingredients": ingredients}
        response = UserActions.send_create_order_request(order_data)
        response_json = response.json()
        assert "order" in response_json

    def test_create_order_with_invalid_ingredients_status_code(self, auth_token):
        invalid_ingredients = ["invalid_hash"]
        order_data = {"ingredients": invalid_ingredients}
        response = UserActions.send_create_order_request(order_data, auth_token)
        assert response.status_code == 400

    def test_create_order_with_invalid_ingredients_error_message(self, auth_token):
        invalid_ingredients = ["invalid_hash"]
        order_data = {"ingredients": invalid_ingredients}
        response = UserActions.send_create_order_request(order_data, auth_token)
        response_json = response.json()
        assert response_json.get("message") == "One or more ids provided are incorrect", "Error message is incorrect"

    def test_create_order_with_empty_ingredients_status_code(self, auth_token):
        order_data = {"ingredients": []}
        response = UserActions.send_create_order_request(order_data, auth_token)
        assert response.status_code == 400

    def test_create_order_with_empty_ingredients_error_message(self, auth_token):
        order_data = {"ingredients": []}
        response = UserActions.send_create_order_request(order_data, auth_token)
        response_json = response.json()
        assert response_json.get("message") == "Ingredient ids must be provided", "Error message is incorrect"



