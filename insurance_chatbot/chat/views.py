from django.shortcuts import render

# Create your views here.
# chat/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .rag import rag_answer

def rag_view(request):
    answer = None
    question = None

    if request.method == "POST":
        question = request.POST.get("question", "")
        if question:
            answer = rag_answer(question)

    return render(request, "chat/rag_view.html", {"question": question, "answer": answer})