from django.contrib import admin
from .models import Holiday, CalendarDiary

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('H_name', 'H_date', 'H_country', 'H_memo')  # 리스트에서 보여줄 필드들
    search_fields = ('H_name', 'H_country')  # 검색할 수 있는 필드들

@admin.register(CalendarDiary)
class CalendarDiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status', 'user')  # 리스트에서 보여줄 필드들
    search_fields = ('title', 'user__username')  # 검색할 수 있는 필드들
    list_filter = ('status', 'user')  # 필터링할 수 있는 필드들