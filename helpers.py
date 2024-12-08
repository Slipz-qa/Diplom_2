import random
import string

class Helper:

    @staticmethod
    def generate_unique_email():
        """Генерирует уникальный email"""
        return f"test_{''.join(random.choices(string.ascii_lowercase, k=8))}@example.com"