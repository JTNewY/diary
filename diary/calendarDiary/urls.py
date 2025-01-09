from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main_page, name='main'),
    path('holidays/', views.holiday_list, name='holiday_list'),
    path('calendar/', views.calendar_view, name='calendar_view'),  # 기본 경로
    path('calendar/<str:username>/', views.calendar_view, name='calendar_view_by_user'),  # username 경로
    path('calendar/<str:username>/<str:selected_date>/', views.calendar_view, name='calendar_view_by_date'),  # 날짜 경로
    path('calendar/<str:username>/<str:start_date>/<str:end_date>/', views.calendar_events, name='calendar_events'),
    path('add_task/', views.add_task, name='add_task'),
]