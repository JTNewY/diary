from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomLoginForm



# 로그인 뷰
def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"{username}님, 환영합니다!")
                # 로그인 후 캘린더 페이지로 리다이렉트, username을 URL로 전달
                return redirect('calendar_view', username=username)  # calendar_view로 리다이렉트
            else:
                messages.error(request, "로그인 정보가 올바르지 않습니다.")
        else:
            messages.error(request, "양식을 올바르게 작성해주세요.")
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form})

# 로그인 페이지 뷰
def accounts_login(request):
    if request.method == 'POST':
        # Retrieve ID and PASSWORD from the form
        user_id = request.POST.get('id')  # Matches the "id" field in your form
        password = request.POST.get('password')  # Matches the "password" field in your form

        # Authenticate the user
        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            # Login the user
            login(request, user)    
            messages.success(request, f"{user.username}님, 환영합니다!")
            # return redirect('calendar_view', username=user_id)  # Redirect to the desired page
        else:
            # Invalid login credentials
            messages.error(request, "ID 또는 비밀번호가 잘못되었습니다.")
    # Render the login page for GET requests or invalid submissions
    else:
        return render(request, 'login/index.html')
    return render(request, 'login/index.html')

# 회원가입 페이지 뷰
def accounts_signup(request):
    return render(request, 'login/signup.html')

# 아이디 찾기 뷰
def accounts_find_id(request):
    return render(request, 'login/find_id.html')

# 비밀번호 찾기 뷰
def accounts_find_pw(request):
    return render(request, 'login/find_pw.html')

# 로그아웃
def accounts_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "로그아웃 완료")
    else:
        messages.error(request, "이미 로그아웃 중")
    return redirect("../login")
