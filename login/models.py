from django.db import models, forms

# Create your models here.

class Login(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(widget=forms.PasswordInput, max_length=20)
     