from django.db import models
from django.conf import settings
from django.utils import timezone

class ToDo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # settings.AUTH_USER_MODEL을 사용하여 CustomUser 모델을 참조
        on_delete=models.CASCADE, 
        related_name="user_todos"  # 가독성을 위해 명확한 이름 사용
    )
    task = models.CharField(max_length=255)  # To-Do 내용
    due_date = models.DateField(null=True, blank=True)  # 마감일을 선택적으로 변경
    is_completed = models.BooleanField(default=False)  # 완료 여부

    class Meta:
        ordering = ['-due_date']  # 최신 마감일이 위에 표시되도록 정렬

    def __str__(self):
        return f"{self.task} ({'완료' if self.is_completed else '미완료'})"


class Note(models.Model):
    content = models.TextField()  # 메모 내용
    date = models.DateField(default=timezone.now)  # 현재 날짜를 기본값으로 설정
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # settings.AUTH_USER_MODEL을 사용하여 CustomUser 모델을 참조
        on_delete=models.CASCADE, 
        null=True,  # null=True로 설정하여 기존 데이터를 처리할 수 있도록 함
        blank=True  # blank=True로 설정하여 Admin에서 빈 값도 허용
    )

    def __str__(self):
        return f"Note: {self.content[:20]}"  # 간단히 메모의 처음 20자만 출력


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(default=timezone.now)  # 기본값으로 현재 날짜 설정

    def __str__(self):
        return self.title


class Holiday(models.Model):
    H_name = models.CharField(verbose_name="공휴일 이름", max_length=100)
    H_date = models.DateField(verbose_name="공휴일 날짜")
    H_memo = models.CharField(verbose_name="공휴일 설명", max_length=255, blank=True)
    H_country = models.CharField(
        verbose_name="국가코드",
        max_length=2,
        choices=[("KR", "South Korea"), ("US", "United States"), ("JP", "Japan")],
    )

    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"
        ordering = ["H_date"]

    def __str__(self):
        return f"{self.H_name} ({self.H_date})"


class CalendarDiary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 사용자와 연결
        on_delete=models.CASCADE,
        related_name="user_diaries"
    )
    title = models.CharField(max_length=255)  # 일정 제목
    start_date = models.DateTimeField()  # 시작 일시
    end_date = models.DateTimeField()  # 종료 일시
    content = models.TextField(blank=True)  # 내용
    color = models.CharField(max_length=7, default="#FFFFFF")  # 색상
    status = models.CharField(
        max_length=50,
        choices=[('planned', 'Planned'), ('completed', 'Completed'), ('canceled', 'Canceled')],
        default='planned'
    )
    notification_time = models.DateTimeField(null=True, blank=True)  # 알림 시간
    add_task = models.CharField(max_length=255, blank=True, null=True)  # add_task 필드를 추가

    class Meta:
        ordering = ['-start_date']  # 최신 일정이 위에 표시되도록 정렬

    def __str__(self):
        return f"{self.title} ({self.start_date} - {self.end_date})"
