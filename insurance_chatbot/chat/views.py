from django.shortcuts import render

# Create your views here.
# chat/views.py
import json, os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# def rag_view(request):
#     # --- GET 요청: 페이지 렌더링 ---
#     if request.method == "GET":
#         return render(request, "chat/rag_view.html")

#     # --- POST 요청: JSON / form-data 처리 ---
#     elif request.method == "POST":
#         question = ""
#         # 💡 file_content 대신 file_path 변수를 사용합니다.
#         file_path = None 

#         content_type = request.META.get("CONTENT_TYPE", "").lower()

#         try:
#             if "application/json" in content_type:
#                 data = json.loads(request.body.decode('utf-8'))
#                 question = data.get("question", "")
#                 # JSON 요청 시 파일 처리는 없으므로 file_path는 None으로 유지
#             else:
#                 question = request.POST.get("question", "")
#                 if request.FILES.get('file'):
#                     uploaded_file = request.FILES['file']
#                     save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
                    
#                     with open(save_path, 'wb+') as f:
#                         for chunk in uploaded_file.chunks():
#                             f.write(chunk)
                    
#                     # 💡 파일 경로를 변수에 저장합니다.
#                     file_path = save_path
#                     # 💡 여기서 파일 내용을 읽을 필요가 없습니다. rag_answer가 처리합니다.

#         except Exception as e:
#             return JsonResponse({"error": f"Request parse error: {str(e)}"}, status=400)

#         if not question:
#             return JsonResponse({"error": "No question provided"}, status=400)

#         # RAG 호출
#         try:
#             # ✅ 수정된 부분:
#             # 1. 키워드를 file_path로 변경
#             # 2. 값으로 파일 경로(file_path 변수)를 전달
#             from .rag import rag_answer
#             answer = rag_answer(question=question, file_path=file_path)
#         except Exception as e:
#             return JsonResponse({"error": f"rag_answer error: {str(e)}"}, status=500)

#         return JsonResponse({"answer": answer})

#     return JsonResponse({"error": "Invalid request method"}, status=405)
   
   
def rag_view(request):
    # --- GET 요청: 페이지 렌더링 ---
    if request.method == "GET":
        return render(request, "chat/rag_view.html")

    # --- POST 요청: JSON / form-data 처리 ---
    elif request.method == "POST":
        question = ""
        file_path = None

        content_type = request.META.get("CONTENT_TYPE", "").lower()

        try:
            if "application/json" in content_type:
                data = json.loads(request.body.decode("utf-8"))
                question = data.get("question", "")
            else:
                question = request.POST.get("question", "")
                if request.FILES.get("file"):
                    uploaded_file = request.FILES["file"]
                    save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
                    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
                    with open(save_path, "wb+") as f:
                        for chunk in uploaded_file.chunks():
                            f.write(chunk)
                    file_path = save_path

        except Exception as e:
            return JsonResponse({"error": f"Request parse error: {str(e)}"}, status=400)

        if not question:
            return JsonResponse({"error": "No question provided"}, status=400)

        try:
            from .rag import rag_answer
            answer = rag_answer(question=question, file_path=file_path)
        except Exception as e:
            return JsonResponse({"error": f"rag_answer error: {str(e)}"}, status=500)

        return JsonResponse({"answer": answer})

    return JsonResponse({"error": "Invalid request method"}, status=405)


def login_view(request):
    if request.method == 'POST':
        # AuthenticationForm을 상속받은 폼은 request와 data를 함께 전달합니다.
        form = LoginForm(request=request, data=request.POST)
        
        # is_valid()는 아이디/비밀번호가 올바른지 DB와 대조하여 확인합니다.
        if form.is_valid():
            # 유효성 검증이 성공하면, 인증된 사용자 객체를 가져옵니다.
            user = form.get_user()
            
            # 🚀 가장 중요한 부분: 사용자에게 입장 도장(세션)을 찍어줍니다.
            login(request, user)
            
            # 로그인 성공 후, 'home'이라는 이름의 URL로 이동시킵니다.
            return redirect('home')
    else:
        # GET 요청일 경우, 빈 폼을 생성합니다.
        form = LoginForm()
        
    # 로그인 실패 시(is_valid() 실패) 또는 GET 요청 시,
    # 에러 메시지가 포함된 폼과 함께 login.html을 다시 보여줍니다.
    return render(request, 'chat/login.html', {'form': form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()     # DB에 새 사용자 저장
            login(request, user)   # 회원가입 직후 로그인 처리
            return redirect("/")   # 원하는 페이지로 이동 (예: 홈)
    else:
        form = UserCreationForm()

    return render(request, "chat/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('home')