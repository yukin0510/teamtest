from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views import generic
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.views.generic import ListView,TemplateView,UpdateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class IndexView(TemplateView):
    template_name = 'users/index.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/edit.html'
    success_url = reverse_lazy('users:users')

    def get_object(self, queryset=None):
        # URL から渡された pk を使って、特定のユーザーを取得
        user_id = self.kwargs.get("pk")
        return get_object_or_404(CustomUser, pk=user_id)

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('equipment:list')  # 登録完了後にリダイレクトするURL
    template_name = 'users/sign_up.html'

class CustomUserListView(LoginRequiredMixin,ListView):
    template_name = 'users/users.html'
    model = CustomUser
    context_object_name = 'users'

    def get_queryset(self):
        return CustomUser.objects.order_by('-registration_date')
    
    def dispatch(self, request, *args, **kwargs):#管理者以外にユーザー一覧へのアクセスを許可しない
        # ログインユーザーのis_adminがTrueかどうかをチェック
        if not request.user.is_admin:
            return HttpResponseForbidden("このページにアクセスする権限がありません。")
        return super().dispatch(request, *args, **kwargs)