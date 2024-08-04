from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.views.generic import ListView,TemplateView
from .models import CustomUser

class IndexView(TemplateView):
    template_name = 'users/index.html'

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')  # 登録完了後にリダイレクトするURL
    template_name = 'users/sign_up.html'

class CustomUserListView(ListView):
    template_name = 'users/users.html'
    model = CustomUser
    context_object_name = 'users'