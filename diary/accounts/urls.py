from django.urls import path
from .views import custom_login_view

app_name = "accounts"

urlpatterns = [
    path('login/', custom_login_view, name='login'),
    
]