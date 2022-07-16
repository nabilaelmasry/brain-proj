from django.urls import path
from .views import UserRecords, RegisterUser, LogoutView, ResetPassword
from rest_framework.authtoken import views

app_name = 'patient'
urlpatterns = [
    path('login/', views.obtain_auth_token, name='login'),
    path('users/', UserRecords.as_view(), name='users'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/', ResetPassword.as_view(), name="reset-password"),
]
