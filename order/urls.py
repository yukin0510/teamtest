from django.urls import path
from .views import OrderListView

app_name = 'order'
urlpatterns = [
    path('', OrderListView.as_view(), name='history'),
]