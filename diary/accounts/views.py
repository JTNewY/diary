from django.shortcuts import render

# Create your views here.

# 로그인 페이지 뷰
def accounts_login(request):
    return render(request, 'login/index.html')  # login.html로 변경

# 회원가입 페이지 뷰
# def accounts_signup(request):
#    return render(request, 'signup.html')  # signup.html로 변경