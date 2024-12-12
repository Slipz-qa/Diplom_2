import random
import string
import allure
from data import user_data

class Helper:

    @staticmethod
    @allure.step("Генерация уникального email")
    def generate_unique_email():

        return f"test_{''.join(random.choices(string.ascii_lowercase, k=8))}@example.com"

    @staticmethod
    @allure.step("Получение данных пользователя")
    def get_user_data():

        return user_data