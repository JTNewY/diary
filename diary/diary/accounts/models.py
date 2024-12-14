from django.contrib.auth.models import AbstractUser
from django.db import models

# 장고에 생년월일 추가
class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)