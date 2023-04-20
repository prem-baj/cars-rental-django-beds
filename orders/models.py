from django.db import models
from cars.models import Car

# Create your models here.


class Order(models.Model):
    PAYMENT_METHODS = (
        ('1', 'Card'),
        ('2', 'Cash'),
    )
    #customer = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_up_date = models.DateTimeField(blank=False, null=False)
    drop_off_date = models.DateTimeField(blank=False, null=False)
    payment_method = models.CharField(max_length=1, choices=PAYMENT_METHODS)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.car} => {self.pick_up_date} => {self.drop_off_date}"
