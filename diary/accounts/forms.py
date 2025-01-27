from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label='사용자 이름'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='비밀번호'
    )

# 아이디 찾기 폼
class FindUsernameForm(forms.Form):
    first_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'email']
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("이름을 입력해주세요.")
        return first_name 

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("이메일을 입력해주세요.")
        return email