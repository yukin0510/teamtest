from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Equipment,StockChange
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EquipForm, StockUpdateForm
from order.forms import OrderForm
from order.models import Order



class EquipListView(LoginRequiredMixin, ListView):
    template_name = 'equipment/equip_list.html'
    model = Equipment
    context_object_name = 'equipment'

    def get_queryset(self):
        return Equipment.objects.order_by('-created_at')

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

    def get_context_data(self, **kwargs):#画像がエラーになった時用の回避策
        context = super().get_context_data(**kwargs)
        equip = context['equip']
        context['image_url'] = equip.image.url if equip.image else '/static/images/no_image.jpg'# 画像URLが空の場合、デフォルト画像URLを設定
        context['stock_update_form'] = StockUpdateForm(instance=equip) #在庫数更新のフォームが使えるようになる
        context['stock_changes'] = StockChange.objects.filter(equip=equip).order_by('-changed_date')[:5]
        context['order_form'] = OrderForm() #発注数更新
        context['orders'] = Order.objects.filter(equip=equip)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        previous_stock = self.object.stock# フォームを保存する前に、更新前の在庫数を取得しておく

    # 在庫数更新フォームの処理
        stock_update_form = StockUpdateForm(request.POST, instance=self.object)
        if stock_update_form.is_valid():
        # フォームを保存する
            updated_equip = stock_update_form.save()

        # StockChangeテーブルに変更履歴を保存
            StockChange.objects.create(
            equip=self.object,
            user=request.user,
            previous_stock=previous_stock,
            new_stock=updated_equip.stock,
        )

            return redirect(self.get_success_url())

        # 発注フォームの処理
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.equip = self.object
            order.user = request.user
            order.save()
            return redirect(self.get_success_url())

        # 発注承認処理
        order_id = request.POST.get('approve_order')
        if order_id:
            order = get_object_or_404(Order, pk=order_id)
            order.approve(request.user)


        return self.render_to_response(self.get_context_data(
            stock_update_form=stock_update_form,
            order_form=order_form
        ))

    def get_success_url(self):
        return reverse_lazy('equipment:detail', kwargs={'pk': self.object.pk})
    

class EquipUpdateView(LoginRequiredMixin, UpdateView):
    model = Equipment
    form_class = EquipForm
    template_name = 'equipment/edit.html'
    
    def get_success_url(self):
        return reverse_lazy('equipment:detail', kwargs={'pk': self.object.pk})

class EquipDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment:list')

