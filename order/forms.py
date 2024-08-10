from .models import Order
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
        labels = {
         'quantity': '発注数',
      }
        
class OrderApprovalForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []  # フォームのフィールドは空にします。POSTリクエストでフォームが提出されたときに、`approve` メソッドを呼び出します。