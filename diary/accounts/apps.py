from django.apps import AppConfig
from django.contrib.auth import get_user_model
from datetime import date

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'