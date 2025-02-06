from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomLoginForm, FindUsernameForm, FindPasswordForm,ResetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from .models import CustomUser
import random
import string


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
    form = FindUsernameForm()
    
    if request.method == 'POST':
        form = FindUsernameForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            user = CustomUser.objects.filter(first_name=first_name, email=email).first()  
            if user:
                messages.success(request, f'아이디는 {user.username}입니다.')
                return redirect('auth:login')
            else:
                messages.error(request, '아이디 찾기에 실패했습니다.')
        else:
            messages.error(request, '입력한 값이 올바르지 않습니다.')

    return render(request, 'accounts/find_id.html', {'form': form, 'message_class': 'col-4 mx-auto'})

# 비밀번호 찾기 뷰
def accounts_find_pw(request):
    form = FindPasswordForm()     
    if request.method == 'POST':
        form = FindPasswordForm(request.POST)  
        if form.is_valid():  
            first_name = form.cleaned_data['first_name']
            username = form.cleaned_data['username']
            user = CustomUser.objects.filter(first_name=first_name, username=username).first() 
            if user:
                new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) 
                user.set_password(new_password)  
                user.save()  
                messages.success(request, f'비밀번호가 초기화되었습니다. 새로운 비밀번호는 {new_password}입니다.')
                return redirect('accounts:login')  
            else:
                messages.error(request, '사용자를 찾을 수 없습니다. 이름과 아이디를 다시 확인해주세요.')
        else:
            messages.error(request, '입력한 값이 올바르지 않습니다.')
    return render(request, 'accounts/find_pw.html', {'form': form})

# 비밀번호 초기화 뷰
def accounts_reset_pw(request):
    # GET 요청 시 폼을 빈 상태로 초기화
    form = ResetPasswordForm()

    # 이미 로그인한 사용자라면, 프로필 페이지로 리다이렉트
    if request.user.is_authenticated:
        return redirect('auth:profile')

    # POST 요청 시
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)  # 폼에 POST 데이터 바인딩

        if form.is_valid():  # 폼 검증
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']

            # 사용자 정보로 사용자 검색
            user = CustomUser.objects.filter(first_name=first_name, email=email, username=username).first()

            if user:
                # 새 비밀번호 생성
                new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                user.set_password(new_password)
                user.save()
                # 비밀번호 초기화 성공 메시지
                messages.success(request, f'비밀번호가 초기화되었습니다. 새로운 비밀번호는 {new_password}입니다.')
                return redirect('auth:login')
            else:
                # 사용자 찾을 수 없는 경우
                messages.error(request, '입력한 정보로 사용자를 찾을 수 없습니다.')
        else:
            # 폼이 유효하지 않으면 오류 메시지
            messages.error(request, '입력된 정보에 오류가 있습니다. 다시 시도해주세요.')

    # GET 또는 잘못된 POST 시 폼을 템플릿에 전달
    return render(request, 'accounts/reset_pw.html', {'form': form})

# 로그아웃
def accounts_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "로그아웃 완료")
    else:
        messages.error(request, "이미 로그아웃 중")
    return redirect("../login")
