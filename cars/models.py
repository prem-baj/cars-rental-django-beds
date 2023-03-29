from django.db import models

# Create your models here.

from django.db import models

# bmw
class CarBrand(models.Model):
    name = models.CharField(max_length=200)

# passat
class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

# details
class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    production_date = models.DateTimeField('Production date')
    colour = models.CharField(max_length=200, default ="red")

    def __str__(self):
        return f"{self.model.brand.name} {self.model.name} {self.name}"
