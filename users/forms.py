from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # カスタムユーザーモデルを取得
        fields = ('email', 'username','is_staff','is_admin') 
        labels = {
         'username':'ユーザー名',
         'email': 'email',
         'is_staff': 'スタッフとして登録する',
         'is_admin': '管理者として登録する',
      }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'is_staff', 'is_admin')
        labels = {
            'username': 'ユーザー名',
            'email': 'email',
            'is_staff': 'スタッフとして登録する',
            'is_admin': '管理者として登録する',
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('このユーザー名は既に使用されています。')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('このメールアドレスは既に使用されています。')
        return email