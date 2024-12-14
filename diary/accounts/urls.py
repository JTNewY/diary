from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.accounts_login, name='login'),
    path('signup/', views.accounts_signup, name='signup'),
    path('find_id/', views.accounts_find_id, name='find_id'),
    path('find_pw/', views.accounts_find_pw, name="find_pw"),
    
]