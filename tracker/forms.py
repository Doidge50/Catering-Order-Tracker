from django import forms
from .models import *
from django.core.validators import RegexValidator



class LoginUserForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class OrderForm(forms.Form):


        class Meta:

            
            ITEM_CHOICES = [
                ('Fish and Chips', 'Fish and Chips'),
                ('Chips', 'Chips')
            ]

            TABLE_NUMBER_CHOICES = [([x,x]) for x in range(1,21)]

            model = Order
            fields = ['item', 'numberOfOrders', 'tableNumber']
            labels = {
                 'item': 'Item',
                 'numberOfOrders' : 'Quantity',
                 'tableNumber' : 'Table Number',
            }
            widgets = {
                 'item' : forms.Select(choices = ITEM_CHOICES),
                 'tableNumber' : forms.Select(choices = TABLE_NUMBER_CHOICES)
            }