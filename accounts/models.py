from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from .constants import ACCOUNT_TYPE,GENDER_TYPE
class UserBankAccount(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='account')
    account_no=models.IntegerField(unique=True)
    account_type=models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    gender_type=models.CharField(max_length=10,choices=GENDER_TYPE)
    birth_date=models.DateField()
    initial_deposite_date=models.DateField(auto_now_add=True)
    balance=models.DecimalField(default=0,max_digits=12,decimal_places=2)
    def __str__(self):
        return str(self.account_no)
class UserAddress(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='address')
    street_address=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    def __str__(self):
        return self.country
    
    

    


