# chat/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="아이디")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
