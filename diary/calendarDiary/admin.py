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
    list_display = ('title', 'start_date', 'end_date', 'status', 'user', 'add_task')  # 리스트에서 보여줄 필드들
    search_fields = ('title', 'user__username')  # 검색할 수 있는 필드들
    list_filter = ('status', 'user')  # 필터링할 수 있는 필드들

    def add_task(self, obj):
        # CalendarDiary에서 add_task 필드를 반환하도록 수정
        return obj.add_task  # 실제 add_task 필드가 있다면 그것을 반환

    add_task.admin_order_field = 'add_task'  # admin에서 정렬 가능하게 하려면 필드명 지정
    add_task.short_description = 'Add Task'  # admin에서 보일 필드 이름을 설정

    def user(self, obj):
        # CalendarDiary의 user 필드에서 CustomUser 모델의 필드를 가져옵니다.
        return obj.user.username  # obj.user가 CustomUser 모델을 참조하고 있으므로 username을 출력

    user.admin_order_field = 'user'  # admin에서 정렬 가능하게 하려면 필드명 지정
    user.short_description = 'User'  # admin에서 보일 필드 이름을 설정
