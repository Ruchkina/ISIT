# """
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('hello/', views.hello, name='hello'),
#     path('helloBmstu/', views.index, name='index'),
#     path('', views.hello, name='hello'),
# ]
# """
# from django.urls import path
# from django.contrib import admin
#
# from . import views
#
# app_name = 'shop'
# urlpatterns = [
#     path('', views.GetPerformanceList, name='all'),
#     path('product/<int:id>/', views.GetPerformance, name='performance_url'),
#     path('sendText', views.sendText, name='sendText'),
#     path('deletePerform', views.DeletePerform, name='DeletePerform'),
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'performance', views.PerformanceViewSet)
router.register(r'theatre', views.TheatreViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'customer', views.CustomerViewSet)
# router.register(r'qwe', views.qweViewSet, basename='qwe')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path("GetPerformanceList", view=views.GetPerformanceList, name="GetPerformanceList"),
]