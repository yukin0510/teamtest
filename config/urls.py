from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('admin/', admin.site.urls),  # 管理画面を有効化する場合
    path('equipment/', include('equipment.urls')),  # equipment アプリの URL
    path('order_history/', include('order.urls')),  # orderアプリの URL
    path('', include('users.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)