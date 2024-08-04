from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView
from .models import Equipment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EquipForm


class EquipListView(LoginRequiredMixin, ListView):
    template_name = 'equipment/equip_list.html'
    model = Equipment
    context_object_name = 'equipment'

class EquipCreateView(LoginRequiredMixin, CreateView):
    template_name = 'equipment/add.html'
    model = Equipment
    form_class = EquipForm  # フォームクラスを指定
    success_url = reverse_lazy('equipment:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EquipDetailView(LoginRequiredMixin, DetailView):
    model = Equipment
    template_name = 'equipment/detail.html'
    context_object_name = 'equip' #ここの名前でテンプレート上で呼び出す