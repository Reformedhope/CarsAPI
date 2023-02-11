from django.db import models

# Create your models here.
class car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2) # doesnt round in unpredictable ways. Have to include how many digits are going to be in this feild