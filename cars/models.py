from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# bmw
class CarBrand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

# passat
class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.brand.name} {self.name}"

# details
class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    production_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(9999)],
        default=2020
    )
    colour = models.CharField(max_length=200, default ="red")

    def __str__(self):
        return f"{self.model.brand.name} {self.model.name} {self.name}"
