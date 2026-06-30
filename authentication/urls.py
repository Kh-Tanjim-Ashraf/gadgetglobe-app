from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from authentication.views import register

urlpatterns = [
    path('login/', LoginView.as_view(
            template_name='authentication/login.html', 
            redirect_authenticated_user=True
        ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', view=register, name='register'),
]
