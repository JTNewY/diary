from django.shortcuts import render, redirect
from .models import Holiday, CalendarDiary, Note, Event, ToDo
from django.contrib.auth.decorators import login_required
from datetime import datetime

# 메인 페이지 뷰
def main_page(request):
    return render(request, 'main/main.html')  # 'base.html'로 변경 가능

# 공휴일 목록
def holiday_list(request):
    holidays = Holiday.objects.all()  # 모든 공휴일 불러오기
    return render(request, 'holidays.html', {'holidays': holidays})

# 캘린더 뷰 (To-Do와 Event 가져오기)
@login_required
def calendar_view(request, selected_date=None):
    if selected_date:
        selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    else:
        selected_date = datetime.today().date()

    # 해당 날짜의 To-Do와 이벤트 가져오기
    todos = ToDo.objects.filter(user=request.user, due_date=selected_date)
    events = Event.objects.filter(start_date__date=selected_date)

    # 기존 노트 데이터 (추후 DB 연동 시 실제 데이터로 대체 가능)
    notes = Note.objects.filter(user=request.user)

    return render(request, 'calendar.html', {
        'selected_date': selected_date,
        'todos': todos,
        'events': events,
        'notes': notes
    })

# To-Do 추가 뷰
@login_required
def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        due_date = request.POST.get('due_date')

        # 새로운 To-Do 항목 추가
        ToDo.objects.create(user=request.user, task=task, due_date=due_date)
        
        # 일정 후 캘린더 페이지로 리다이렉트
        return redirect('calendar_view', selected_date=due_date)
    
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
            return redirect('calendar_view', selected_date=todo.due_date)
        except ToDo.DoesNotExist:
            return redirect('calendar_view', selected_date=datetime.today().date())

    return redirect('calendar_view', selected_date=datetime.today().date())
