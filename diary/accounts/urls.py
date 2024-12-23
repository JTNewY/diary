from django.urls import path
from .views import custom_login_view, accounts_find_id, accounts_find_pw, accounts_login, accounts_signup, accounts_logout

app_name = "accounts"

urlpatterns = [
    path('loginsam/', custom_login_view, name='loginsam'),
    path('signup/', accounts_signup, name='signup'),
    path('find_id/', accounts_find_id, name='find_id'),
    path('find_pw/', accounts_find_pw, name='find_pw'),
    path('login/', accounts_login, name='login'),
    path('logout/', accounts_logout, name='logout'),
]