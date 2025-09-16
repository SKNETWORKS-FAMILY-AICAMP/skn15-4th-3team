from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# 1. 회원가입 폼
# users/forms.py

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    # 1. Meta 클래스: 폼의 기본 설정을 담당하는 부분
    class Meta(UserCreationForm.Meta):
        model = User
        # ✅ 이 폼에 포함할 필드 목록 (가장 중요!)
        fields = ('username', 'password1', 'password2')

    # 2. __init__ 메서드: 필드의 라벨, placeholder 등 세부 디자인을 수정하는 부분
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "아이디"
        self.fields['username'].widget.attrs.update({
            'placeholder': '사용할 아이디를 입력하세요',
        })

        self.fields['password1'].label = "비밀번호"
        self.fields['password1'].widget.attrs.update({
            'placeholder': '비밀번호를 입력하세요',
        })
        
        self.fields['password2'].label = "비밀번호 확인"
        self.fields['password2'].widget.attrs.update({
            'placeholder': '비밀번호를 다시 입력하세요',
        })
# 2. 로그인 폼
class LoginForm(AuthenticationForm): # Django 기본 로그인 폼을 상속받아 사용
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "아이디"
        self.fields['username'].widget.attrs.update({
            'placeholder': '아이디를 입력하세요',
        })
        
        self.fields['password'].label = "비밀번호"
        self.fields['password'].widget.attrs.update({
            'placeholder': '비밀번호를 입력하세요',
        })