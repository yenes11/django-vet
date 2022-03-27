from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileView, RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logut'),
    path('profile/', ProfileView.as_view(), name='profile'),
]