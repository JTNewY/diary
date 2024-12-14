from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main_page, name='main'),
    path('holidays/', views.holiday_list, name='holiday_list'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
    path('calendar/<str:username>/<str:selected_date>/', views.calendar_view, name='calendar_view'),
    path('calendar/<str:username>/', views.calendar_view, name='calendar_view'),  # selected_date가 없을 때

]