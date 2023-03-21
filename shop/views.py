
# from django.shortcuts import render
from shop.models import Order
from . import models
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from rest_framework import viewsets
from shop.serializers import qweSerializer, PerformanceSerializer, CustomerSerializer, TheatreSerializer, OrderSerializer, OrderTheatreSerializer
#
# def sendText(request):
#     input_text = request.POST['text']
#     num = int(input_text)
#     return render(request, 'performances.html', {'data': {
#         'performances': Performance.objects.filter(id__range=(0, num))
#     }})
#
# def DeletePerform(request):
#     input_text = request.POST['text']
#     num = int(input_text)
#     Performance.DeletePerform(num)
#     return render(request, 'performances.html', {'data': {
#         'performances': Performance.objects.all()
#     }})
#
# def GetPerformance(request, id):
#     return render(request, 'performance.html', {'data': {
#         'performance': Performance.objects.filter(id=id).first()
#     }})
#
# def GetPerformanceList(request):
#     return render(request, 'performances.html', {'data': {
#         'performances': Performance.objects.all()
#     }})
# # def Get
# #
# #     people = Person.objects.filter(age__lt=35).raw("SELECT * FROM hello_person")

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = models.Performance.objects.all()
    serializer_class = PerformanceSerializer

class TheatreViewSet(viewsets.ModelViewSet):
    queryset = models.Theatre.objects.all()
    serializer_class = TheatreSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = OrderSerializer

class OrderTheatreViewSet(viewsets.ModelViewSet):
    queryset = models.OrderTheatre.objects.all()
    serializer_class = OrderTheatreSerializer

def GetPerformanceList(request):
    d = '2023-03-06'
    return render(request, 'qwe.html', {
            'data1': Order.objects.filter(data = d).count()
         # .values('data')
         # .annotate(total=Count('pk'))
    })

         # .values('data')
         # .annotate(total=Count('pk'))
         # .filter('data' == '2023-04-20'))
# class qweViewSet(viewsets.ModelViewSet):
#     queryset = models.Order.func()
    # queryset = models.OrderTheatre.objects.all()
    # queryset = orders.filter(pk=1)
    # serializer_class = qweSerializer