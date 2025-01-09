from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Holiday, Note, Event, ToDo,CalendarDiary
from accounts.models import CustomUser  # CustomUser 모델을 가져옴
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

def add_task(request):
    if request.method == 'POST':
        try:
            task_name = request.POST.get('task_name')
            description = request.POST.get('description')
            start_date = request.POST.get('start_date')
            start_time = request.POST.get('start_time')
            end_date = request.POST.get('end_date')
            end_time = request.POST.get('end_time')
            color = request.POST.get('color')

            # 로그로 값 출력
            print(f"Received data: task_name={task_name}, start_date={start_date}, start_time={start_time}, end_date={end_date}, end_time={end_time}, color={color}")

            # 필수 필드 유효성 검사
            if not task_name or not start_date or not start_time or not end_date or not end_time:
                return JsonResponse({'success': False, 'message': '모든 필드를 채워주세요.'}, status=400)

            # 날짜 및 시간 병합
            try:
                start_datetime = datetime.combine(
                    datetime.strptime(start_date, "%Y-%m-%d").date(),
                    datetime.strptime(start_time, "%H:%M").time()
                )
                end_datetime = datetime.combine(
                    datetime.strptime(end_date, "%Y-%m-%d").date(),
                    datetime.strptime(end_time, "%H:%M").time()
                )
            except ValueError as e:
                return JsonResponse({'success': False, 'message': '날짜와 시간이 올바르지 않습니다.'}, status=400)

            # 일정 저장
            CalendarDiary.objects.create(
                user=request.user,
                title=task_name,
                start_date=start_datetime,
                end_date=end_datetime,
                content=description,
                color=color  # 색상 저장
            )

            return JsonResponse({'success': True, 'message': '일정이 추가되었습니다.'})
        
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'success': False, 'message': '서버 오류가 발생했습니다. 다시 시도해주세요.'}, status=500)

    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'}, status=400)
@login_required
def calendar_view(request, username=None, selected_date=None):
    # 사용자 처리
    if username:
        user = get_object_or_404(CustomUser, username=username)
    else:
        user = request.user

    # 선택된 날짜가 없으면 오늘 날짜로 설정
    if selected_date:
        events = CalendarDiary.objects.filter(user=user, start_date__date=selected_date)
    else:
        events = CalendarDiary.objects.filter(user=user)  # 모든 일정 가져오기

    events_data = [{
        'id': event.id,
        'title': event.title,
        'start_date': event.start_date,
        'end_date': event.end_date,
        'color': event.color,
        'content': event.content,
    } for event in events]

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # is_ajax() 대신 사용
        return JsonResponse({'events': events_data})

    context = {
        'events': events,
        'selected_date': selected_date,
        'username': username,
    }
    return render(request, 'main/calendar.html', context)

# 메인 페이지 뷰
def main_page(request):
    return render(request, 'main/main.html')  # 'base.html'로 변경 가능

# 공휴일 목록
def holiday_list(request):
    holidays = Holiday.objects.all()  # 모든 공휴일 불러오기
    return render(request, 'holidays.html', {'holidays': holidays})
def calendar_events(request, username, start_date, end_date):
    # start_date와 end_date를 날짜 형식으로 변환 (시간까지 포함한 정확한 범위)
    start_date = datetime.strptime(start_date, '%Y-%m-%d')  # 예: '2024-12-01'
    end_date = datetime.strptime(end_date, '%Y-%m-%d')  # 예: '2024-12-10'

    # 끝 날짜를 하루의 마지막 시간으로 설정 (23:59:59.999999)
    end_date = end_date.replace(hour=23, minute=59, second=59, microsecond=999999)

    # 사용자의 일정 데이터를 가져옵니다. start_date와 end_date 범위에 해당하는 일정을 필터링
    events = CalendarDiary.objects.filter(
        user__username=username,
        start_date__gte=start_date,
        end_date__lte=end_date
    )

    # 이벤트 데이터를 JSON 형식으로 반환
    events_data = [
        {
            'id': event.id,
            'title': event.title,
            'start_date': event.start_date.strftime('%Y-%m-%d %H:%M'),  # 원본 형식 그대로 반환
            'end_date': event.end_date.strftime('%Y-%m-%d %H:%M') if event.end_date else None,  # 종료일도 원본 형식 그대로
            'color': event.color,  # 색상
            'content': event.content  # 내용
        }
        for event in events
    ]
    
    return JsonResponse({'events': events_data})