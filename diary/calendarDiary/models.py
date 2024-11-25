from django.db import models
from django.conf import settings


class Holiday(models.Model):
    H_name = models.CharField(verbose_name="공휴일 이름", max_length=100)
    H_date = models.DateField(verbose_name="공휴일 날짜")
    H_memo = models.CharField(verbose_name="공휴일 설명", max_length=255, blank=True)
    H_country = models.CharField(
        verbose_name="국가코드",
        max_length=2,
        choices=[
            ("KR", "South Korea"),
            ("US", "United States"),
            ("JP", "Japan"),
            # 필요에 따라 국가 추가
        ],
    )
    
    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"
        ordering = ["H_date"]  # 필드명 수정

    def __str__(self):
        return f"{self.H_name} ({self.H_date})"
    
class CalendarDiary(models.Model):
    user = models.ForeignKey( # 생일을 추가했음으로 추가해줘야함
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="diaries"
    )
    title = models.CharField(max_length=255)  # 일정 제목
    start_date = models.DateTimeField()  # 일정 시작일
    end_date = models.DateTimeField()  # 일정 종료일
    color = models.CharField(max_length=7, default="#FFFFFF")  # 일정 색깔
    status = models.CharField(max_length=50, choices=[
        ('planned', 'Planned'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ], default='planned')
    content = models.TextField(blank=True)  # 일정 내용
    notification_time = models.DateTimeField(null=True, blank=True)  # 알림 시간

    def __str__(self):
        return f"{self.title} ({self.start_date} - {self.end_date})"

    class Meta:
        ordering = ['-start_date']
    