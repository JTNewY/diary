from django.core.management.base import BaseCommand
from calendarDiary.api import fetch_japan_holidays  # 위에서 작성한 함수 import

class Command(BaseCommand):
    help = "Fetch Japan public holidays from API"

    def handle(self, *args, **kwargs):
        fetch_japan_holidays()
