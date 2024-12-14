from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Holiday, Note, Event, ToDo
from accounts.models import CustomUser  # CustomUser 모델을 가져옴


# 작업 추가 뷰
@login_required
def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        start_time = request.POST.get('start_time')
        end_date = request.POST.get('end_date')
        end_time = request.POST.get('end_time')

        # 시작일과 시작 시간을 datetime 객체로 변환
        start_datetime = datetime.combine(datetime.strptime(start_date, "%Y-%m-%d").date(), 
                                          datetime.strptime(start_time, "%H:%M").time())
        
        # 마감일과 마감 시간을 datetime 객체로 변환
        end_datetime = datetime.combine(datetime.strptime(end_date, "%Y-%m-%d").date(), 
                                        datetime.strptime(end_time, "%H:%M").time())

        # Event 모델에 새 이벤트 추가
        Event.objects.create(
            user=request.user,
            title=task_name,
            description=task_description,
            start_date=start_datetime,
            end_date=end_datetime
        )

        # 일정 추가 후 캘린더 페이지로 리다이렉트
        return redirect('calendar_view', username=request.user.username, selected_date=start_date)
    
    return render(request, 'add_todo.html')
# 캘린더 뷰 (사용자별 캘린더 페이지)
@login_required
def calendar_view(request, username=None, selected_date=None):
    if username:
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            user = request.user
    else:
        user = request.user

    if selected_date:
        try:
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
        except ValueError:
            selected_date = datetime.today().date()
    else:
        selected_date = datetime.today().date()

    # 해당 날짜의 To-Do와 이벤트 가져오기
    todos = ToDo.objects.filter(user=user, due_date=selected_date)
    
    # 이벤트 필터링: start_date와 end_date에 맞는 이벤트를 가져옴
    events = Event.objects.filter(start_date__year=selected_date.year,
                                  start_date__month=selected_date.month,
                                  start_date__day=selected_date.day)

    # 템플릿에 데이터 전달
    context = {
        'user': user,
        'selected_date': selected_date,
        'todos': todos,
        'events': events,
    }

    return render(request, 'main/main.html', context)

# To-Do 추가 뷰


# 메인 페이지 뷰
def main_page(request):
    return render(request, 'main/main.html')  # 'base.html'로 변경 가능

# 공휴일 목록
def holiday_list(request):
    holidays = Holiday.objects.all()  # 모든 공휴일 불러오기
    return render(request, 'holidays.html', {'holidays': holidays})
