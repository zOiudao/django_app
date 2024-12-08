from django.db import models

# Create your models here.
class CreateUser(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80, unique=True)
    cpf = models.CharField(max_length=14, unique=True)