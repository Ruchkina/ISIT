"""
from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('helloBmstu/', views.index, name='index'),
    path('', views.hello, name='hello'),
]
"""
from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.GetPerformanceList, name='all'),
    path('product/<int:id>/', views.GetPerformance, name='performance_url'),
    path('sendText', views.sendText, name='sendText'),
    # path('da', views.da, name='da'),    # path('product/1/', views.GetPr1, name='product1'),
    # path('product/2/', views.GetPr2, name='product2'),
    # path('product/3/', views.GetPr3, name='product3'),
    # path('order/<int:id>/', views.GetProduct, name='product_url'),
]