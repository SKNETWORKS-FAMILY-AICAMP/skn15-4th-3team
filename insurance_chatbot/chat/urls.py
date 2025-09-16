from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("rag_view/", views.rag_view, name="rag_view"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path('logout/', views.logout_view, name='logout'),
    path("", views.rag_view, name="home"),  # 홈 페이지
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
