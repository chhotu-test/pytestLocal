import random
import string
from datetime import datetime, timedelta


class TestDataHelper:
    
    @staticmethod
    def generate_random_string(length: int = 10) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    @staticmethod
    def generate_random_email() -> str:
        username = TestDataHelper.generate_random_string(8)
        domain = random.choice(['gmail.com', 'yahoo.com', 'test.com', 'example.com'])
        return f"{username}@{domain}"
    
    @staticmethod
    def generate_random_password(length: int = 12) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))
    
    @staticmethod
    def generate_random_username(length: int = 8) -> str:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    @staticmethod
    def get_current_timestamp() -> str:
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    @staticmethod
    def get_future_date(days: int = 1) -> str:
        future_date = datetime.now() + timedelta(days=days)
        return future_date.strftime("%Y-%m-%d")
    
    @staticmethod
    def get_past_date(days: int = 1) -> str:
        past_date = datetime.now() - timedelta(days=days)
        return past_date.strftime("%Y-%m-%d")
