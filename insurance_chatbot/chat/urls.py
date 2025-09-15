from django.urls import path
from . import views

urlpatterns = [
    path("rag_view/", views.rag_view, name="rag_view"),
]