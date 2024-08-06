from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from .models import Equipment,StockChange
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EquipForm, StockUpdateForm


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
        # 画像URLが空の場合、デフォルト画像URLを設定
        context['image_url'] = equip.image.url if equip.image else '/static/images/no_image.jpg'
        context['stock_update_form'] = StockUpdateForm(instance=equip) #在庫数更新
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = StockUpdateForm(request.POST, instance=self.object)
        if form.is_valid():
            # 在庫数の変更前の値を保存
            previous_stock = self.object.stock
            # フォームを保存（在庫数を更新）
            updated_equip = form.save()

            # StockChangeテーブルに変更履歴を保存
            StockChange.objects.create(
                equip=self.object,
                user=request.user,
                previous_stock=previous_stock,
                new_stock=updated_equip.stock,
            )
            return redirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(stock_update_form=form))

    def get_success_url(self):
        return reverse_lazy('equipment:detail', kwargs={'pk': self.object.pk})
    

class EquipUpdateView(UpdateView):
    model = Equipment
    form_class = EquipForm
    template_name = 'equipment/edit.html'
    success_url = reverse_lazy('equipment:list')

