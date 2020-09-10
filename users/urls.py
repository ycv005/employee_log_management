from django.urls import path
from .views import SignUpView, LoginView, logout_view


app_name = 'users'

urlpatterns = [
    path("login/", LoginView.as_view(), name='login_page'),
    path("signup/", SignUpView.as_view(), name='signup_page'),
    path("logout/", logout_view, name='logout'),
]
