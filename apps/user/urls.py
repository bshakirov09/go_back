# Django
from django.urls import path

# Project
from user.views.change_password import ChangePasswordView
from user.views.me import UserMeAPIVIew
from user.views.signup import SignupView
from user.views.update import UserUpdateAPIView, UserAvatarUpdate
from user.views.verify_email import EmailVerifyView
from user.views.resend_verify_code import ResendVerifyCodeView
from user.views.login import LoginView, LoginSocialNetworkView
from user.views.forgot_password import (
    SendForgotPasswordCodeView, CheckForgotPasswordCodeView, ForgotPasswordView
)
from user.views.delete_account import DeleteAccountView

user_auth = [
    path('signup/', SignupView.as_view()),
    path('verify_email/', EmailVerifyView.as_view()),
    path('resend_verify_code/', ResendVerifyCodeView.as_view()),
    path('login/', LoginView.as_view()),
    path('login_with_social_network/', LoginSocialNetworkView.as_view()),
    path('login/', LoginView.as_view()),
    path('send_forgot_password_code/', SendForgotPasswordCodeView.as_view()),
    path('check_forgot_password_code/', CheckForgotPasswordCodeView.as_view()),
    path('set_new_password_with_forgot_password/', ForgotPasswordView.as_view()),
    path('delete_account/', DeleteAccountView.as_view())
]

urlpatterns = [
    path('update/', UserUpdateAPIView.as_view()),
    path('update/avatar/', UserAvatarUpdate.as_view()),
    path('me/', UserMeAPIVIew.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
]
urlpatterns += user_auth
