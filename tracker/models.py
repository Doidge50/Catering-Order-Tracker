from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator


class User(AbstractUser):
    username = models.EmailField(unique=True, blank=False)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name = 'order')
    item = models.CharField(max_length = 20, blank  = False)
    numberOfOrders = models.IntegerField(blank = False, validators= 
                        [MinValueValidator(0, 'Cant have negative orders')])
    timeOrdered = models.DateTimeField(blank = False)
    tableNumber = models.IntegerField(blank = False)
