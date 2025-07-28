from django.urls import path
from .views.register import RegisterView
from .views.login import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]
