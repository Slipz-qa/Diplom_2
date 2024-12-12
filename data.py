BASE_URL = "https://stellarburgers.nomoreparties.site/api"
HEADERS = {'Content-Type': 'application/json'}
from helpers import Helper


user_data = {
    "email": Helper.generate_unique_email(),
    "password": "testpass123",
    "name": "Test User"
}


