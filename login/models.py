from django.db import models

# Create your models here.

class Login(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=20)



#If I want this I need to push it.
   
    