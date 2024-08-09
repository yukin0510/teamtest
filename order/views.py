from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order

# Create your views here.
class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'order/history.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.order_by('-order_date')