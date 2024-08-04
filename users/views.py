from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.views.generic import ListView,TemplateView,UpdateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'users/index.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/edit.html'
    success_url = reverse_lazy('users:users')

    def get_object(self):
        return self.request.user

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('equipment:list')  # 登録完了後にリダイレクトするURL
    template_name = 'users/sign_up.html'

class CustomUserListView(LoginRequiredMixin,ListView):
    template_name = 'users/users.html'
    model = CustomUser
    context_object_name = 'users'