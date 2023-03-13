
from django.urls import path
from django.contrib import admin

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.GetPerformanceList, name='all'),
    path('product/<int:id>/', views.GetPerformance, name='performance_url'),
    path('sendText', views.sendText, name='sendText'),
    path('admin/', admin.site.urls),
]