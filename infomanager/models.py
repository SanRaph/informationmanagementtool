from datetime import datetime
from django.db import models


# Create your models here.
class Info(models.Model):
    GENDER = [('Male', 'Male'), ('Female', 'Female')]

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.IntegerField(unique=True)
    gender = models.CharField(choices=GENDER, default='Male', blank=True, max_length=10)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
