from django.contrib import admin
from .models import Holiday, CalendarDiary
from accounts.models import CustomUser  # CustomUser 모델 import

# CustomUser 모델을 admin에 등록
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')  # CustomUser에서 표시할 필드들
    search_fields = ('username', 'email')  # 검색할 수 있는 필드들


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('H_name', 'H_date', 'H_country', 'H_memo')  # 리스트에서 보여줄 필드들
    search_fields = ('H_name', 'H_country')  # 검색할 수 있는 필드들

@admin.register(CalendarDiary)
class CalendarDiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status', 'user', 'add_task')  # add_task 필드 추가
    search_fields = ('title', 'user__username')
    list_filter = ('status', 'user')

    def user(self, obj):
        return obj.user.username  # 사용자의 username을 표시

    user.admin_order_field = 'user'
    user.short_description = 'User'

    def add_task(self, obj):
        return obj.add_task  # add_task 필드 값을 반환

    add_task.admin_order_field = 'add_task'  # 정렬 필드를 지정
    add_task.short_description = 'Add Task'  # Admin에서 필드명 지정