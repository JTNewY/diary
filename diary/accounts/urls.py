from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.accounts_login, name='login'),
#    path('signup/', views.accounts_signup, name='signup'),
]