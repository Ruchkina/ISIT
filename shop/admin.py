from django.contrib import admin
from .models import Theatre
from .models import Order
from .models import Customer
from .models import OrderTheatre
from .models import Performance


admin.site.register(Performance)
admin.site.register(Theatre)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderTheatre)

# Register your models here.
