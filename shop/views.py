
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def index(request):
    return HttpResponse("Hello, world. You're at the shop index.")

def hello(request):
    return render(request, 'products.html', {
        'current_date': date.today()
    })

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# def GetOrders(request):
#     return render(request, 'products.html')
#
# def GetOrder(request, id):
#     return render(request, 'order.html', {'data' : {
#         'current_date': date.today(),
#         'id': id
#     }})

# def start(request):
#     return render(request, 'products.html', {'data': {
#         'products': [
#             {'title': 'Какая-то штука номер 1', 'id': 1},
#             {'title': 'Какая-то штука номер 2', 'id': 2},
#             {'title': 'Какая-то штука номер 3', 'id': 3},
#         ]
#     }})
# <!--a href="{% url 'product-detail' product.id %}"><img alt="" src="{{ product.image.url }}"></a>
# </html>-->

# , 'image': 'static /assets/first.jpg'

def GetProduct(request, id):
    return render(request, 'product.html', {'data' : {
        'id': id
    }})

def GetProd(request, id):
    return render(request, 'prod.html', {'data' : {
        'id': id
    }})

def start(request):
    return render(request, 'products.html', {'data': {
        'products': [
            {'title': 'Какая-то штука номер 1', 'id': 1},
            {'title': 'Какая-то штука номер 2', 'id': 2},
            {'title': 'Какая-то штука номер 3', 'id': 3},
        ]
    }})

def sendText(request):
    input_text = request.POST['text']


