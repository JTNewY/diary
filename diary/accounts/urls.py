from django.urls import path


urlpatterns = [
    path('login/', 'accounts.views.login_view', name='login'),
    path('signup/', 'accounts.views.signup_view', name='signup'),
    # 이렇게 함으로써 순환 참조를 피할 수 있음
]