from django.db import models

# Create your models here.
class Pizza(models.Model):
    nombre = models.CharField(max_length=255)

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
