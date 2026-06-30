from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from authentication.views import register

urlpatterns = [
    # Authentication
    path('login/', LoginView.as_view(
            template_name='authentication/login.html', 
            redirect_authenticated_user=True
        ), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', view=register, name='register'),
    
    # Password Change
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/change-password.html'
        ), name='change-password'),
    
    path('change-password-successful/', PasswordChangeDoneView.as_view(
        template_name='authentication/change-password-successful.html'
    ), name='password_change_done'),
]
