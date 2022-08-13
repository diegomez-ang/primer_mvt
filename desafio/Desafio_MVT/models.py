from django.db import models
import datetime

class Familiares(models.Model):
    name = models.CharField(max_length=30)
    num_id = models.IntegerField()
    date_birth = models.CharField(max_length=15)
