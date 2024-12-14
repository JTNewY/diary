from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_date',)}),  # 생년월일 필드를 추가
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birth_date',)}),
    )
