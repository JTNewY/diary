from django.shortcuts import render

# Create your views here.

# 로그인 페이지 뷰
def accounts_login(request):
    return render(request, 'login/index.html')  # login.html로 변경

# 회원가입 페이지 뷰
def accounts_signup(request):
    return render(request, 'login/signup.html')

# 아이디 찾기 뷰
def accounts_find_id(request):
    return render(request, 'login/find_id.html')

# 비밀번호 찾기 뷰
def accounts_find_pw(request):
    return render(request, 'login/find_pw.html')
