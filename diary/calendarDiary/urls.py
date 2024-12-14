from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main_page, name='main'),  
    path('calendar/', views.calendar_view, name='calendar'),    # 캘린더 페이지
    path('calendar/<int:year>/<int:month>/<int:day>/', views.calendar_view, name='calendar_view'),
]