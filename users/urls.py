from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'users/index.html'


app_name = "users"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/sign_in.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]