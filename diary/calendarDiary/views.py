from django.shortcuts import render
from .models import Holiday, CalendarDiary,Note, Event,ToDo
from django.utils import timezone
from datetime import datetime

# Create your views here.
def main_page(request):
    return render(request, 'main/main.html')  # 'base.html'로 변경 가능

# 공휴일 목록
def holiday_list(request):
    holidays = Holiday.objects.all()  # 모든 공휴일 불러오기
    return render(request, 'holidays.html', {'holidays': holidays})

def calendar_view(request, selected_date=None):
    if selected_date:
        selected_date = datetime.strptime(selected_date, "%Y-%m-%d")
    else:
        selected_date = datetime.today()

    # 예시 데이터: 실제로는 DB에서 이벤트 데이터를 가져올 수 있습니다.
    notes = [
        {'content': 'My note 1'},
        {'content': 'My note 2'}
    ]
    events = [
        {'title': 'Event 1', 'start_date': datetime(2023, 12, 10)},
        {'title': 'Event 2', 'start_date': datetime(2023, 12, 15)}
    ]

    return render(request, 'calendar.html', {
        'selected_date': selected_date,
        'notes': notes,
        'events': events
    })
    
def calendar_view(request, selected_date=None):
    if selected_date:
        selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    else:
        selected_date = datetime.today().date()

    todos = ToDo.objects.filter(user=request.user, due_date=selected_date)
    events = Event.objects.filter(start_date__date=selected_date)

    return render(request, 'calendar.html', {
        'selected_date': selected_date,
        'todos': todos,
        'events': events
    })

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        due_date = request.POST.get('due_date')
        ToDo.objects.create(user=request.user, task=task, due_date=due_date)
        return redirect('calendar_view')
    return render(request, 'add_todo.html')