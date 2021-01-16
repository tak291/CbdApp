from django.contrib import admin
from .models import Login, Job, Worker

# Register your models here.

admin.site.register(Login)
admin.site.register(Job)
admin.site.register(Worker)
