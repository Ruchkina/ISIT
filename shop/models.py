from django.db import models

class Theatre(models.Model):
    director = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Performance(models.Model):
    name = models.CharField(max_length=30)
    theatre = models.ForeignKey(
        Theatre,
        on_delete=models.CASCADE,
        default=None
    )
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/assets/', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    data_perform = models.DateField(blank=True, null=True)
    # def DeletePerform(self, idp):
    #     self.objects.filter(idp=self.pk).delete()
class Customer (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
class Order (models.Model):
    data = models.DateField()
    customer_rk = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
class OrderTheatre(models.Model):
    order_rk = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    performance_rk = models.ForeignKey(
        Performance,
        on_delete=models.CASCADE
    )




# Create your models here.
