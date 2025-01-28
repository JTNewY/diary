import requests
from .models import Holiday

def fetch_japan_holidays():
    url = "https://date.nager.at/api/v3/PublicHolidays/2025/JP"
    response = requests.get(url)

    if response.status_code == 200:
        holidays = response.json()
        for holiday in holidays:
            Holiday.objects.update_or_create(
                H_name=holiday["localName"],
                H_date=holiday["date"],
                H_country="JP"
            )
        print("일본 공휴일 데이터가 업데이트되었습니다.")
    else:
        print("API 요청 실패:", response.status_code)