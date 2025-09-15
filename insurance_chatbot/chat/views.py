from django.shortcuts import render

# Create your views here.
# chat/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .rag import rag_answer

@api_view(["POST"])
def rag_view(request):
    question = request.data.get("question", "")
    if not question:
        return Response({"error": "question is required"}, status=400)

    answer = rag_answer(question)
    return Response({"question": question, "answer": answer})
