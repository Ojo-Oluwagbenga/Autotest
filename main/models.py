from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    itemcode = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20)
    matric = models.CharField(default="non_student", max_length=20)

