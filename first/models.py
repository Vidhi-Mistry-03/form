from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class post(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(max_length=50)
        
    def __str__(self):
        return self.name

