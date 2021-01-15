from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Login(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    phone_number = PhoneNumberField(max_length=10, default='')

class Customer(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)


class Worker(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

class Job(models.Model):
    jobid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Worker = models.ForeignKey(Worker, on_delete=models.CASCADE)






   
