from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.accounts_login, name='login'),
    path('signup/', views.accounts_signup, name='signup'),
    # 이렇게 함으로써 순환 참조를 피할 수 있음
]