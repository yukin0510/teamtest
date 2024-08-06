from django.urls import path
from .views import EquipListView,EquipCreateView,EquipDetailView,EquipUpdateView,EquipDeleteView

app_name = 'equipment'
urlpatterns = [
    path('', EquipListView.as_view(), name='list'),
    path('add/', EquipCreateView.as_view(), name='add'),
    path('<int:pk>', EquipDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', EquipUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', EquipDeleteView.as_view(), name='delete'),
]