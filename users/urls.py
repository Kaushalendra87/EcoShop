from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .forms import LoginForm, StyledPasswordResetForm, StyledSetPasswordForm
from . import views

urlpatterns =[
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        authentication_form=LoginForm,
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='myapp:index'), name='logout'),
    path('profile/', views.profile, name='profile'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html',
        email_template_name='users/password_reset_email.html',
        subject_template_name='users/password_reset_subject.txt',
        form_class=StyledPasswordResetForm,
        success_url=reverse_lazy('password_reset_done'),
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html',
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        form_class=StyledSetPasswordForm,
        success_url=reverse_lazy('password_reset_complete'),
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html',
    ), name='password_reset_complete'),

    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
    path('email-verification-sent/', views.email_verification_sent, name='email-verification-sent'),
    path('email-verification-failed/', views.email_verification_failed, name='email-verification-failed'),
    path('email-verification-success/', views.email_verification_success, name='email-verification-success'),
]

