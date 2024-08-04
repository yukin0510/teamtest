from django.urls import path
from .views import EquipListView,EquipCreateView,EquipDetailView

app_name = 'equipment'
urlpatterns = [
    path('', EquipListView.as_view(), name='list'),
    path('add/', EquipCreateView.as_view(), name='add'),
    path('<int:pk>', EquipDetailView.as_view(), name='detail'),
]