from django.db import models

# Create your models here.
class Car(models.Model):
    FUEL_CHOICES = [
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('Electric','Electric'),
        ('Hybrid','Hybrid')
        ]
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    fuel_type = models.CharField(max_length=10,choices=FUEL_CHOICES)
    
    def __str__(self):
        return f"{self.make}{self.model} ({self.year})"
    