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

    OPEN = 1
    PENDING_APPOINTMENT =  2 
    CLOSED = 3

    STATUS_CHOICE = (
        (OPEN, '    open'),
        (PENDING_APPOINTMENT, 'pending'),
        ( CLOSED, 'closed' ),
        )

    status = models.IntegerField(choices=STATUS_CHOICE,default=1)
    customer = models.CharField(max_length=200,default=1)
    Worker = models.ForeignKey(Worker, on_delete=models.CASCADE)






   
