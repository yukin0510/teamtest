from django.shortcuts import render
from django.views.generic import ListView
from .models import Equipment
from django.contrib.auth.mixins import LoginRequiredMixin


class ListView(LoginRequiredMixin, ListView):
    template_name = 'equipment/equip_list.html'
    model = Equipment
    context_object_name = 'equipment'