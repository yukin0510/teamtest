from django.urls import path
from .views import ListView

app_name = 'equipment'
urlpatterns = [
    path('', ListView.as_view(), name='list'),
]