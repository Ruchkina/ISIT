
# from django.shortcuts import render
# from shop.models import Performance
from . import models

from rest_framework import viewsets
from shop.serializers import PerformanceSerializer, CustomerSerializer, TheatreSerializer, OrderSerializer, OrderTheatreSerializer
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