
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from shop.models import Performance


def sendText(request):
    input_text = request.POST['text']
    num = int(input_text)
    return render(request, 'performances.html', {'data': {
        'performances': Performance.objects.filter(id__range=(0, num))
    }})


def GetPerformance(request, id):
    return render(request, 'performance.html', {'data': {
        'performance': Performance.objects.filter(id=id).first()
    }})

def GetPerformanceList(request):
    return render(request, 'performances.html', {'data': {
        'performances': Performance.objects.all()
    }})


