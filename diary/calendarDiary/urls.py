from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main_page, name='main'),
    path('holidays/', views.holiday_list, name='holiday_list'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('add_task/', views.add_task, name='add_task'),  # add_task URL 추
    path('<str:username>/<str:selected_date>/', views.calendar_view, name='calendar_view'),
    path('<str:username>/', views.calendar_view, name='calendar_view'),  
]