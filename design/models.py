from django.db import models

# Create your models here.
class event(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=50)
    day = models.CharField(max_length=20)
    startTime = models.CharField(max_length=20)
    endTime = models.CharField(max_length=20)
    details = models.CharField(max_length=100)