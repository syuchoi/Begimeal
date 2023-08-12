from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, LogoutAPIView

urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('current', UserRetrieveUpdateAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
]