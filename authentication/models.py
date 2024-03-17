# from django.db import models

# class user(models.Model):
#     name = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     address = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# # Create your models here.
from django.db import models
from django.contrib.auth.models import User

