from django.db import models

# Create your models here.

from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=200)


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    production_date = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.model.brand.name} {self.model.name} {self.name}"
