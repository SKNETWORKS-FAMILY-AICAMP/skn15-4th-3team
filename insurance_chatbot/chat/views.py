from django.shortcuts import render

# Create your views here.
# chat/views.py
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .rag import rag_answer
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def signup_view(request):
    return render(request, 'chat/signup.html')

def rag_view(request):
    # --- GET 요청: 페이지 렌더링 ---
    if request.method == "GET":
        return render(request, "chat/rag_view.html")

    # --- POST 요청: JSON / form-data 처리 ---
    elif request.method == "POST":
        question = ""
        
        # content_type을 정확하게 확인
        content_type = request.META.get("CONTENT_TYPE", "").lower()
        
        try:
            # JSON 요청 처리
            if "application/json" in content_type:
                data = json.loads(request.body.decode('utf-8')) # 디코딩 추가
                question = data.get("question", "")
            # form-data 또는 x-www-form-urlencoded 요청 처리
            else:
                question = request.POST.get("question", "")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Request parse error: {str(e)}"}, status=400)

        # 질문이 없을 경우
        if not question:
            return JsonResponse({"error": "No question provided"}, status=400)

        try:
            answer = rag_answer(question)
        except Exception as e:
            # rag_answer 함수에서 발생하는 특정 에러를 명시적으로 처리하는 것이 더 좋습니다.
            # 예: return JsonResponse({"error": "RAG process failed: " + str(e)}, status=500)
            return JsonResponse({"error": f"rag_answer error: {str(e)}"}, status=500)

        return JsonResponse({"answer": answer})

    # --- 그 외 메서드 ---
    return JsonResponse({"error": "Invalid request method"}, status=405) # 405 Method Not Allowed가 더 적절
    


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # 로그인 성공 후 이동할 url name
            else:
                form.add_error(None, "아이디 또는 비밀번호가 올바르지 않습니다.")
    else:
        form = LoginForm()
    return render(request, "chat/login.html", {"form": form})