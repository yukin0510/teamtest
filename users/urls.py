from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import CustomUserListView,IndexView,SignUpView,UserUpdateView




app_name = "users"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users/', CustomUserListView.as_view(), name='users'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='edit'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/sign_in.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]