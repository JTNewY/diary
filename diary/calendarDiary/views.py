from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Holiday, Note, Event, ToDo
from accounts.models import CustomUser  # CustomUser 모델을 가져옴

# 캘린더 뷰 (사용자별 캘린더 페이지)
@login_required
def calendar_view(request, username=None, selected_date=None):
    # username이 URL에서 전달되면 해당 사용자 가져오기, 없으면 로그인한 사용자
    if username:
        try:
            user = CustomUser.objects.get(username=username)  # CustomUser 모델 사용
        except CustomUser.DoesNotExist:
            user = request.user  # 사용자가 없으면 로그인한 사용자로 대체
    else:
        user = request.user  # 로그인한 사용자

    # selected_date 처리: URL에서 날짜가 전달되면 해당 날짜로, 없으면 오늘 날짜
    if selected_date:
        try:
            selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()  # 날짜 형식으로 변환
        except ValueError:
            selected_date = datetime.today().date()  # 날짜 형식이 맞지 않으면 오늘 날짜로 설정
    else:
        selected_date = datetime.today().date()  # selected_date가 없으면 오늘 날짜

    # 해당 날짜의 To-Do와 이벤트 가져오기
    todos = ToDo.objects.filter(user=user, due_date=selected_date)
    
    # 이벤트 필터링: start_date가 selected_date와 일치하는 이벤트를 가져옴
    events = Event.objects.filter(start_date__year=selected_date.year,
                                  start_date__month=selected_date.month,
                                  start_date__day=selected_date.day)

    # 기존 노트 데이터
    notes = Note.objects.filter(user=user)

    # 템플릿에 데이터 전달
    context = {
        'user': user,
        'selected_date': selected_date,
        'todos': todos,
        'events': events,
        'notes': notes
    }

    # calendar.html로 렌더링
    return render(request, 'main/main.html', context)

# To-Do 추가 뷰
@login_required
def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        due_date = request.POST.get('due_date')

        # 새로운 To-Do 항목 추가
        ToDo.objects.create(user=request.user, task=task, due_date=due_date)
        
        # 일정 후 캘린더 페이지로 리다이렉트
        return redirect('calendar_view', username=request.user.username, selected_date=due_date)
    
    return render(request, 'add_todo.html')

# To-Do 삭제 뷰
@login_required
def delete_todo(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        try:
            # To-Do 항목 삭제
            todo = ToDo.objects.get(id=task_id, user=request.user)
            todo.delete()
            return redirect('calendar_view', username=request.user.username, selected_date=todo.due_date)
        except ToDo.DoesNotExist:
            return redirect('calendar_view', username=request.user.username, selected_date=datetime.today().date())

    return redirect('calendar_view', username=request.user.username, selected_date=datetime.today().date())

# 메인 페이지 뷰
def main_page(request):
    return render(request, 'main/main.html')  # 'base.html'로 변경 가능

# 공휴일 목록
def holiday_list(request):
    holidays = Holiday.objects.all()  # 모든 공휴일 불러오기
    return render(request, 'holidays.html', {'holidays': holidays})
