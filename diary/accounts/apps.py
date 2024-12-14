from django.apps import AppConfig
from django.contrib.auth import get_user_model
from datetime import date

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
            self.create_dummy_user()

    @staticmethod
    def create_dummy_user():
        User = get_user_model()
        if not User.objects.filter(username='dummyuser').exists():
            User.objects.create_user(
                username='dummyuser',
                email='dummyuser@example.com',
                password='securepassword123',
                birth_date=date(1990, 5, 15)
            )